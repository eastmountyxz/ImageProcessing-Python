# -*- coding: utf-8 -*-
# By：Eastmount CSDN 2021-06-07
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('te.png')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
#双边滤波
result = cv2.bilateralFilter(source, 15, 150, 150)

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#显示图形
titles = ['原始图像', '双边滤波']  
images = [source, result]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
