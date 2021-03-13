# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-03-12
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('lena.bmp')

#灰度转换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#直方图均衡化处理
result = cv2.equalizeHist(gray)

#显示图像
plt.subplot(221)
plt.imshow(gray, cmap=plt.cm.gray), plt.axis("off"), plt.title('(a)') 
plt.subplot(222)
plt.imshow(result, cmap=plt.cm.gray), plt.axis("off"), plt.title('(b)') 
plt.subplot(223)
plt.hist(img.ravel(), 256), plt.title('(c)') 
plt.subplot(224)
plt.hist(result.ravel(), 256), plt.title('(d)') 
plt.show()
