# -*- coding: utf-8 -*-
# 2021-05-17 Eastmount CSDN
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取图像
img=cv2.imread('scenery.png')
grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

#阈值化处理
ret,thresh1=cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)  
ret,thresh2=cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY_INV)  
ret,thresh3=cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)  
ret,thresh4=cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO)  
ret,thresh5=cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO_INV)

#显示结果
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC',
'TOZERO','TOZERO_INV']  
images = [grayImage, thresh1, thresh2, thresh3, thresh4, thresh5]  
for i in range(6):  
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()
