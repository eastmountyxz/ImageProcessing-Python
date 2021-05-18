# -*- coding: utf-8 -*-
# 2021-05-17 Eastmount CSDN
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread('scenery.png')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#阈值化处理
ret, binary = cv2.threshold(grayImage, 0, 255,
                            cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

#边缘检测
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE) 

#轮廓绘制
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

#显示图像5
cv2.imshow('gray', binary)
cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
