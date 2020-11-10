# -*- coding: utf-8 -*-
# BY:Eastmount CSDN 2020-11-10
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('lena.png')

#获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

#创建一幅图像
new_img = np.zeros((height, width, 3), np.uint8)

#图像量化操作 量化等级为2
for i in range(height):
    for j in range(width):
        for k in range(3): #对应BGR三分量
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 128
            new_img[i, j][k] = np.uint8(gray)
        
#显示图像
cv2.imshow("src", img)
cv2.imshow("Quantization", new_img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
