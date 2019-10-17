# -*- coding: utf-8 -*-
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('lena.png')
lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#高斯滤波
gaussianBlur = cv2.GaussianBlur(grayImage, (3,3), 0)

#阈值处理
ret, binary = cv2.threshold(gaussianBlur, 127, 255, cv2.THRESH_BINARY)

#Scharr算子
x = cv2.Scharr(grayImage, cv2.CV_32F, 1, 0) #X方向
y = cv2.Scharr(grayImage, cv2.CV_32F, 0, 1) #Y方向
absX = cv2.convertScaleAbs(x)       
absY = cv2.convertScaleAbs(y)
Scharr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

#Canny算子
gaussian = cv2.GaussianBlur(grayImage, (3,3), 0) #高斯滤波降噪
Canny = cv2.Canny(gaussian, 50, 150) 

#LOG算子
gaussian = cv2.GaussianBlur(grayImage, (3,3), 0) #先通过高斯滤波降噪
dst = cv2.Laplacian(gaussian, cv2.CV_16S, ksize = 3) #再通过拉普拉斯算子做边缘检测
LOG = cv2.convertScaleAbs(dst)

#效果图
titles = ['Source Image', 'Gray Image', 'Binary Image',
          'Scharr Image','Canny Image', 'LOG Image']  
images = [lenna_img, grayImage, binary, Scharr, Canny, LOG]  
for i in np.arange(6):  
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
