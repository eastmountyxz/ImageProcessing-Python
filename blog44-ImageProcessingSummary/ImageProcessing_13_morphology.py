#encoding:utf-8
#By:Eastmount CSDN 2021-08-20
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#读取图片
src = cv2.imread('na.png', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)

# 转化为灰度图
Grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 1、消除椒盐噪声：
# 中值滤波器
median = cv2.medianBlur(Grayimg, 5)
# 消除噪声图
cv2.imshow("median-image", median)

# 2、直方图均衡化：
equalize = cv2.equalizeHist(median)
cv2.imshow('hist', equalize)

# 3、二值化处理：
# 阈值为140
ret, binary = cv2.threshold(equalize, 127, 255,cv2.THRESH_BINARY)
cv2.imshow("binary-image",binary)
cv2.waitKey(0)

#设置卷积核
kernel = np.ones((10,10), np.uint8)
close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

#图像开运算
kernel = np.ones((10,10), np.uint8) 
open1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", close)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#图像开运算
kernel = np.ones((10,10), np.uint8) 
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

# Sobel算子 XY方向求梯度 cv2.CV_8U
x = cv2.Sobel(close, cv2.CV_32F, 1, 0, ksize = 3) #X方向
y = cv2.Sobel(close, cv2.CV_32F, 0, 1, ksize = 3) #Y方向
#absX = cv2.convertScaleAbs(x)   # 转回uint8    
#absY = cv2.convertScaleAbs(y)
#Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
gradient = cv2.subtract(x, y)
sobel = cv2.convertScaleAbs(gradient)
cv2.imshow('Sobel', sobel)
cv2.waitKey(0)

#循环显示图形
titles = [ 'source', 'gray', 'median', 'equalize', 'binary', 'close', 'open', 'gradient', 'sobel']  
images = [img, Grayimg, median, equalize, binary, close, open1, gradient, sobel]  
for i in range(9):  
   plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
