#coding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('lena.bmp')

#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#二进制阈值化处理
r, result = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

#计算原图的直方图
hist = cv2.calcHist([img], [0], None, [256], [0,256])

#计算阈值化处理的直方图
hist_res = cv2.calcHist([result], [0], None, [256], [0,256])

#原始图像
plt.figure(figsize=(8, 6))
plt.subplot(221), plt.imshow(img, 'gray'), plt.title("(a)"), plt.axis('off')

#绘制原始图像直方图
plt.subplot(222), plt.plot(hist), plt.title("(b)"), plt.xlabel("x"), plt.ylabel("y")

#阈值化处理后的图像
plt.subplot(223), plt.imshow(result, 'gray'), plt.title("(c)"), plt.axis('off')

#阈值化处理图像的直方图
plt.subplot(224), plt.plot(hist_res), plt.title("(d)"), plt.xlabel("x"), plt.ylabel("y")
plt.show()
