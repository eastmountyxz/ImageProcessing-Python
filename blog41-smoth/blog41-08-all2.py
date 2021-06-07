# -*- coding: utf-8 -*-
# By：Eastmount CSDN 2021-06-07
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('test01_yn.png')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
#中值滤波
result1 = cv2.medianBlur(source, 3)

#高斯双边滤波
result2 =cv2.bilateralFilter(source, 15, 150, 150)

#均值迁移
result3 = cv2.pyrMeanShiftFiltering(source, 20, 50)

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#显示图形
titles = ['原始图像',  '中值滤波', '双边滤波', '均值迁移']  
images = [source, result1, result2, result3]  
for i in range(4):  
   plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
