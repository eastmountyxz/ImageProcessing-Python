# coding: utf-8
# 2021-05-17 Eastmount CSDN
import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像灰度颜色
img = cv2.imread('scenery.png') 

spatialRad = 100   #空间窗口大小
colorRad = 100     #色彩窗口大小
maxPyrLevel = 2    #金字塔层数

#图像均值漂移分割
dst = cv2.pyrMeanShiftFiltering( img, spatialRad, colorRad, maxPyrLevel)

#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
