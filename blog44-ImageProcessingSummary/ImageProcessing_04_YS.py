# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-08-19
import cv2  
import numpy as np
import matplotlib.pyplot as plt
 
#读取图片
src = cv2.imread("Lena.png")

#获取图像宽和高
rows, cols = src.shape[:2]

#BGR转换为RGB
img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#(1)OpenCV加法运算
m = np.ones(img.shape, dtype="uint8")*100 #图像各像素加100
result1 = cv2.add(img, m)

#(2)OpenCV减法运算
m = np.ones(img.shape, dtype="uint8")*50  #图像各像素减50
result2 = cv2.subtract(img, m)

#(3)画圆形
circle = np.zeros((rows, cols, 3), dtype="uint8")
cv2.circle(circle, (int(rows/2.0), int(cols/2)), 100, (255,0,0), -1)
print(circle.shape,img.size, circle.size)

#(4)OpenCV图像与运算
result4 = cv2.bitwise_and(img, circle)

#(5)OpenCV图像或运算
result5 = cv2.bitwise_or(img, circle)

#(6)OpenCV图像异或运算
result6 = cv2.bitwise_xor(img, circle)

#(7)OpenCV图像非运算
result7 = cv2.bitwise_not(img)

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  #指定默认字体
plt.rcParams['axes.unicode_minus'] = False   #解决保存图像是负号

#显示九张图像
titles = ['原图', 'RGB', '加法', '减法', '圆形', '与运算', '或运算', '异或运算', '非运算']
images = [src, img, result1, result2, circle, result4, result5, result6, result7]
for i in range(9):
   plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()



