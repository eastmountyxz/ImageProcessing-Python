#encoding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#读取图像
src = cv2.imread('Lena.png')

#转换为RGB图像
img_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#计算直方图
histb = cv2.calcHist([src], [0], None, [256], [0,255])
histg = cv2.calcHist([src], [1], None, [256], [0,255])
histr = cv2.calcHist([src], [2], None, [256], [0,255])

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示原始图像和绘制的直方图
plt.subplot(121)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title("(a)Lena原始图像")

plt.subplot(122)
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("(b)直方图曲线")
plt.show()
