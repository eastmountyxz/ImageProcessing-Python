#coding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('Lena.png')

#转换为RGB图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#图像HSV转换
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#计算H-S直方图
hist = cv2.calcHist(hsv, [0,1], None, [180,256], [0,180,0,256])

#原始图像
plt.figure(figsize=(8, 6))
plt.subplot(121), plt.imshow(img_rgb, 'gray'), plt.title("(a)"), plt.axis('off')

#绘制H-S直方图
plt.subplot(122), plt.imshow(hist, interpolation='nearest'), plt.title("(b)")
plt.xlabel("x"), plt.ylabel("y")
plt.show()
