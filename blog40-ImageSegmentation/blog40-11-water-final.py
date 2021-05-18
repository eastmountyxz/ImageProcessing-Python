# coding: utf-8
# 2021-05-17 Eastmount CSDN
import numpy as np
import cv2
from matplotlib import pyplot as plt

#读取原始图像
img = cv2.imread('test01.png')

#图像灰度化处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#图像阈值化处理
ret, thresh = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#图像开运算消除噪声
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

#图像膨胀操作确定背景区域
sure_bg = cv2.dilate(opening,kernel,iterations=3)

#距离运算确定前景区域
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

#寻找未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

#标记变量
ret, markers = cv2.connectedComponents(sure_fg)

#所有标签加一，以确保背景不是0而是1
markers = markers+1

#用0标记未知区域
markers[unknown==255]=0

#分水岭算法实现图像分割
markers = cv2.watershed(img, markers)
img[markers == -1] = [255,0,0]

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#显示图像
titles = [u'标记区域', u'图像分割']  
images = [markers, img]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()
