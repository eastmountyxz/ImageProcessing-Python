# -*- coding: utf-8 -*-
import cv2
import numpy as np

#读取原始图像
img = cv2.imread('scenery.png', 1)

#获取图像的高度和宽度
height, width = img.shape[:2]

#图像灰度处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#创建目标图像
dstImg = np.zeros((height,width,1),np.uint8)

#浮雕特效算法：newPixel = grayCurrentPixel - grayNextPixel + 150
for i in range(0,height):
    for j in range(0,width-1):
        grayCurrentPixel = int(gray[i,j])
        grayNextPixel = int(gray[i,j+1])
        newPixel = grayCurrentPixel - grayNextPixel + 150
        if newPixel > 255:
            newPixel = 255
        if newPixel < 0:
            newPixel = 0
        dstImg[i,j] = newPixel
        
#显示图像
cv2.imshow('src', img)
cv2.imshow('dst',dstImg)

#等待显示
cv2.waitKey()
cv2.destroyAllWindows()
