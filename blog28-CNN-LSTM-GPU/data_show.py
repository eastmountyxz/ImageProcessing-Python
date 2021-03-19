# -*- coding: utf-8 -*-
"""
Created on 2021-03-19
@author: xiuzhang Eastmount CSDN
"""
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------第一步 数据读取------------------------------------
## 读取测数据集
train_df = pd.read_csv("news_dataset_train_fc.csv")
val_df = pd.read_csv("news_dataset_val_fc.csv")
test_df = pd.read_csv("news_dataset_test_fc.csv")
print(train_df.head())

## 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  #指定默认字体 SimHei黑体
plt.rcParams['axes.unicode_minus'] = False   #解决保存图像是负号'

## 查看训练集都有哪些标签
plt.figure()
sns.countplot(train_df.label)
plt.xlabel('Label',size = 10)
plt.xticks(size = 10)
plt.show()

## 分析训练集中词组数量的分布
print(train_df.cutwordnum.describe())
plt.figure()
plt.hist(train_df.cutwordnum,bins=100)
plt.xlabel("词组长度", size = 12)
plt.ylabel("频数", size = 12)
plt.title("训练数据集")
plt.show()


