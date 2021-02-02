#encoding:utf-8
#By:Eastmount CSDN 2021-02-01
import cv2  
import numpy as np
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('test.bmp')
image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#图像平移
#垂直方向 向下平移100
M = np.float32([[1, 0, 0], [0, 1, 100]])
img1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#垂直方向 向上平移100
M = np.float32([[1, 0, 0], [0, 1, -100]])
img2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#水平方向 向右平移100
M = np.float32([[1, 0, 100], [0, 1, 0]])
img3 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#水平方向 向左平移100
M = np.float32([[1, 0, -100], [0, 1, 0]])
img4 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#循环显示图形
titles = [ 'Image1', 'Image2', 'Image3', 'Image4']  
images = [img1, img2, img3, img4]  
for i in range(4):  
   plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
