# -*- coding: utf-8 -*-
import cv2
import numpy as np

#读取原始图像
src = cv2.imread('scenery.png')

#图像灰度处理
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#自定义卷积核
kernel = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])

#图像浮雕效果
output = cv2.filter2D(gray, -1, kernel)

#显示图像
cv2.imshow('Original Image', src)
cv2.imshow('Emboss_1',output)

#等待显示
cv2.waitKey()
cv2.destroyAllWindows()
