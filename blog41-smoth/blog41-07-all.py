# -*- coding: utf-8 -*-
# By：Eastmount CSDN 2021-06-07
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('te.png')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
#均值滤波
result1 = cv2.blur(source, (5,5))
result2 = cv2.blur(source, (10,10))

#方框滤波
result3 = cv2.boxFilter(source, -1, (5,5), normalize=1)
result4 = cv2.boxFilter(source, -1, (2,2), normalize=0)

#高斯滤波
result5 = cv2.GaussianBlur(source, (3,3), 0)
result6 = cv2.GaussianBlur(source, (15,15), 0)

#中值滤波
result7 = cv2.medianBlur(source, 3)

#高斯双边滤波
result8 =cv2.bilateralFilter(source, 15, 150, 150)

#显示图形
titles = ['Source', 'Blur 5*5', 'Blur 10*10', 'BoxFilter 5*5',
          'BoxFilter 2*2', 'GaussianBlur 3*3', 'GaussianBlur 15*15',
          'medianBlur', 'bilateralFilter']  
images = [source, result1, result2, result3,
          result4, result5, result6, result7, result8]  
for i in range(9):  
   plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
