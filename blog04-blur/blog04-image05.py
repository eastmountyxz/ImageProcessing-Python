#encoding:utf-8
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('test01.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
#高斯滤波
result = cv2.GaussianBlur(source, (3,3), 0)

#显示图形
titles = ['Source Image', 'GaussianBlur Image']  
images = [source, result]  
for i in xrange(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
