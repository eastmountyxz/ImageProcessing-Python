#encoding:utf-8
import cv2  
import numpy as np
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('scenery.png')
src = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#图像翻转
#0以X轴为对称轴翻转 >0以Y轴为对称轴翻转 <0X轴Y轴翻转
img1 = cv2.flip(src, 0)
img2 = cv2.flip(src, 1)
img3 = cv2.flip(src, -1)

#显示图形
titles = ['Source', 'Image1', 'Image2', 'Image3']  
images = [src, img1, img2, img3]  
for i in xrange(4):  
   plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
