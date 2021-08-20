#encoding:utf-8
#By:Eastmount CSDN 2021-08-20
import cv2
import math
import numpy as np  
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('miao.png')

#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]

#图像灰度上移变换 DB=DA+50
result1 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        if (int(grayImage[i,j]+50) > 255):
            gray = 255
        else:
            gray = int(grayImage[i,j]+50)
        result1[i,j] = np.uint8(gray)

#图像对比度增强变换 DB=DA*1.5
result2 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        if (int(grayImage[i,j]*1.5) > 255):
            gray = 255
        else:
            gray = int(grayImage[i,j]*1.5)
        result2[i,j] = np.uint8(gray)

#图像对比度增强变换 DB=DA*0.8
result3 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        if (int(grayImage[i,j]*0.8) > 255):
            gray = 255
        else:
            gray = int(grayImage[i,j]*0.8)
        result3[i,j] = np.uint8(gray)

#图像灰度反色变换 DB=255-DA
result4 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = 255 - grayImage[i,j]
        result4[i,j] = np.uint8(gray)

#图像灰度非线性变换：DB=DA×DA/255
result5 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = int(grayImage[i,j])*int(grayImage[i,j]) / 255
        result5[i,j] = np.uint8(gray)   

#图像灰度对数变换
result6 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = 10* math.log(1 + grayImage[i, j])
        result6[i,j] = np.uint8(gray)

#图像灰度伽玛变换
result7 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = 3*pow(grayImage[i, j], 0.8)
        if gray>255:
            gray = 255
        result7[i,j] = np.uint8(gray)

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#显示结果
titles = [u'原始图像', u'灰度图像', u'图像拉伸', u'对比度增强', u'对比度减弱',
          u'图像反色', u'非线性变换', u'对数变换', u'伽马变换']  
images = [img, grayImage, result1, result2, result3, result4, result5, result6, result7]  
for i in range(9):  
   plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()
