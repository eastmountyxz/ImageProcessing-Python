# -*- coding: utf-8 -*-
# 2021-05-17 Eastmount CSDN
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('nv.png')

#灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#设置掩码、fgbModel、bgModel
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

#矩形坐标
rect = (100, 100, 500, 800)

#图像分割
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5,
            cv2.GC_INIT_WITH_RECT)

#设置新掩码：0和2做背景
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

#显示原图
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([]), plt.yticks([])

#使用蒙板来获取前景区域
img = img*mask2[:, :, np.newaxis]
plt.subplot(1,2,2)
plt.imshow(img)
plt.title('Target Image')
plt.colorbar()
plt.xticks([]), plt.yticks([])
plt.show()

