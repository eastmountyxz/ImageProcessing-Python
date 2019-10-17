# -*- coding: utf-8 -*-
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('lena.png')

#获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

#采样转换成8*8区域
numHeight = height/8
numwidth = width/8

#创建一幅图像
new_img = np.zeros((height, width, 3), np.uint8)

#图像循环采样8*8区域
for i in range(8):
    #获取Y坐标
    y = i*numHeight
    for j in range(8):
        #获取X坐标
        x = j*numwidth
        #获取填充颜色 左上角像素点
        b = img[y, x][0]
        g = img[y, x][1]
        r = img[y, x][2]
        
        #循环设置小区域采样
        for n in range(numHeight):
            for m in range(numwidth):
                new_img[y+n, x+m][0] = np.uint8(b)
                new_img[y+n, x+m][1] = np.uint8(g)
                new_img[y+n, x+m][2] = np.uint8(r)
        
#显示图像
cv2.imshow("src", img)
cv2.imshow("Sampling", new_img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
