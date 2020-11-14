# -*- coding: utf-8 -*-
#By:Eastmount CSDN 2020-11-12
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib

#读取图像
img = cv2.imread('miao.png')

#图像灰度化处理
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

#固定值阈值化处理
r, thresh1 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)  

#自适应阈值化处理 方法一
thresh2 = cv2.adaptiveThreshold(grayImage, 255, 
cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#自适应阈值化处理 方法二
thresh3 = cv2.adaptiveThreshold(grayImage, 255, 
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示图像
titles = ['灰度图像', '全局阈值', '自适应平均阈值', '自适应高斯阈值']
#显示图像
titles = ['Gray Image',
          'Global Thresholding',
          'Adaptive Mean Thresholding',
          'Adaptive Gaussian Thresholding']
images = [grayImage, thresh1, thresh2, thresh3]
for i in range(4):
   plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
