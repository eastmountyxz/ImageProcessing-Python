#encoding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#读取图像
src = cv2.imread('lena.bmp')

#计算256灰度级的图像直方图
hist = cv2.calcHist([src], [0], None, [256], [0,255])

#输出直方图大小、形状、数量
print(hist.size)
print(hist.shape)
print(hist)

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示原始图像和绘制的直方图
plt.subplot(121)
plt.imshow(src, 'gray')
plt.axis('off')
plt.title("(a)Lena灰度图像")

plt.subplot(122)
plt.plot(hist, color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("(b)直方图曲线")
plt.show()
