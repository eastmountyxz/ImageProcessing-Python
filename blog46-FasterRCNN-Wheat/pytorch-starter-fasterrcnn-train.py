# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:42:38 2021
@author: xiuzhang
"""
import os
import re
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import albumentations as A
from matplotlib import pyplot as plt
from albumentations.pytorch.transforms import ToTensorV2

import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator
from torch.utils.data import DataLoader, Dataset
from torch.utils.data.sampler import SequentialSampler

from dataset import WheatDataset

#-----------------------------------------------------------------------------
#第一步 函数定义
#----------------------------------------------------------------------------
#提取box的四个坐标
def expand_bbox(x):
    r = np.array(re.findall("([0-9]+[.]?[0-9]*)", x))
    if len(r) == 0:
        r = [-1, -1, -1, -1]
    return r

#训练图像增强 Albumentations
def get_train_transform():
    return A.Compose([
        A.Flip(0.5),
        ToTensorV2(p=1.0)
    ], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels']})

#验证图像增强
def get_valid_transform():
    return A.Compose([
        ToTensorV2(p=1.0)
    ], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels']})

def collate_fn(batch):
    return tuple(zip(*batch))

#-----------------------------------------------------------------------------
#第二步 定义变量并读取数据
#-----------------------------------------------------------------------------
DIR_INPUT = 'data'
DIR_TRAIN = f'{DIR_INPUT}/train'
DIR_TEST = f'{DIR_INPUT}/test'
train_df = pd.read_csv(f'{DIR_INPUT}/train.csv')
print(train_df.shape)

train_df['x'] = -1
train_df['y'] = -1
train_df['w'] = -1
train_df['h'] = -1

#读取box四个坐标
train_df[['x', 'y', 'w', 'h']] = np.stack(train_df['bbox'].apply(lambda x: expand_bbox(x)))
train_df.drop(columns=['bbox'], inplace=True)
train_df['x'] = train_df['x'].astype(np.float)
train_df['y'] = train_df['y'].astype(np.float)
train_df['w'] = train_df['w'].astype(np.float)
train_df['h'] = train_df['h'].astype(np.float)

#获取图像id
image_ids = train_df['image_id'].unique()
valid_ids = image_ids[-665:]
train_ids = image_ids[:-665]
valid_df = train_df[train_df['image_id'].isin(valid_ids)]
train_df = train_df[train_df['image_id'].isin(train_ids)]
print(valid_df.shape, train_df.shape)
print(train_df.head())

"""
(147793, 5)
(25006, 8) (122787, 8)
    image_id  width  height   source      x      y      w      h
0  b6ab77fd7   1024    1024  usask_1  834.0  222.0   56.0   36.0
1  b6ab77fd7   1024    1024  usask_1  226.0  548.0  130.0   58.0
2  b6ab77fd7   1024    1024  usask_1  377.0  504.0   74.0  160.0
3  b6ab77fd7   1024    1024  usask_1  834.0   95.0  109.0  107.0
4  b6ab77fd7   1024    1024  usask_1   26.0  144.0  124.0  117.0
"""

#-----------------------------------------------------------------------------
#第三步 加载数据
#-----------------------------------------------------------------------------
train_dataset = WheatDataset(train_df, DIR_TRAIN, get_train_transform())
valid_dataset = WheatDataset(valid_df, DIR_TRAIN, get_valid_transform())

train_data_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=False,
    num_workers=0,
    collate_fn=collate_fn
)

valid_data_loader = DataLoader(
    valid_dataset,
    batch_size=2,
    shuffle=False,
    num_workers=0,
    collate_fn=collate_fn
)

#-----------------------------------------------------------------------------
#第四步 数据可视化
#-----------------------------------------------------------------------------
#提取训练数据和类别
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
images, targets, image_ids = next(iter(train_data_loader))
images = list(image.to(device) for image in images)
targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
boxes = targets[0]['boxes'].cpu().numpy().astype(np.int32)
sample = images[0].permute(1, 2, 0).cpu().numpy()

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

#绘制小麦目标识别box
for box in boxes:
    cv2.rectangle(sample,
                  (box[0], box[1]),
                  (box[2], box[3]),
                  (255, 0, 0), 3)

    ax.text(box[0], 
            box[1] - 2, 
            '{:s}'.format('wheat'), 
            bbox=dict(facecolor='blue', alpha=0.5),
            fontsize=12, 
            color='white')

ax.set_axis_off()
ax.imshow(sample)
#plt.show()

#-----------------------------------------------------------------------------
#第五步 模型构建
#-----------------------------------------------------------------------------
num_classes = 2  #1 class (wheat) + background
lr_scheduler = None
num_epochs = 1
itr = 1

class Averager:
    def __init__(self):
        self.current_total = 0.0
        self.iterations = 0.0

    def send(self, value):
        self.current_total += value
        self.iterations += 1

    @property
    def value(self):
        if self.iterations == 0:
            return 0
        else:
            return 1.0 * self.current_total / self.iterations

    def reset(self):
        self.current_total = 0.0
        self.iterations = 0.0

#load a model pre-trained on COCO
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

#获取分类器输入特征数量
in_features = model.roi_heads.box_predictor.cls_score.in_features

#replace the pre-trained head with a new one
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

#参数设置
model.to(device)
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
#lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

loss_hist = Averager()
print("Start training....")

# 迭代训练
for epoch in range(num_epochs):
    loss_hist.reset()

    for images, targets, image_ids in train_data_loader:

        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
        for t in targets:
            t['boxes'] = t['boxes'].float()
        
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()
        loss_hist.send(loss_value)
        print("loss is :",loss_value)

        optimizer.zero_grad()
        losses.backward()
        optimizer.step()
        if itr % 50 == 0:
            print(f"Iteration #{itr}/{len(train_data_loader)} loss: {loss_value}")
        itr += 1

    #更新学习率
    if lr_scheduler is not None:
        lr_scheduler.step()
    print(f"Epoch #{epoch} loss: {loss_hist.value}")

torch.save(model.state_dict(), 'fasterrcnn_resnet50_fpn.pth')
print("Next Test....")

#-----------------------------------------------------------------------------
#第六步 模型测试
#-----------------------------------------------------------------------------
images, targets, image_ids = next(iter(valid_data_loader))
images = list(img.to(device) for img in images)
targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
boxes = targets[0]['boxes'].cpu().numpy().astype(np.int32)
sample = images[0].permute(1, 2, 0).cpu().numpy()

model.eval()
cpu_device = torch.device("cpu")

outputs = model(images)
outputs = [{k: v.to(cpu_device) for k, v in t.items()} for t in outputs]
fig, ax = plt.subplots(1, 1, figsize=(16, 8))
for box in boxes:
    cv2.rectangle(sample,
                  (box[0], box[1]),
                  (box[2], box[3]),
                  (220, 0, 0), 3)

ax.set_axis_off()
ax.imshow(sample)
plt.show()



    