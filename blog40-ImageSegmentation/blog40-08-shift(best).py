# coding: utf-8
# 2021-05-17 Eastmount CSDN
import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像灰度颜色
img = cv2.imread('scenery.png') 

#获取图像行和列
rows, cols = img.shape[:2]

#mask必须行和列都加2且必须为uint8单通道阵列
mask = np.zeros([rows+2, cols+2], np.uint8) 

spatialRad = 100 #空间窗口大小
colorRad = 100   #色彩窗口大小
maxPyrLevel = 2  #金字塔层数

#图像均值漂移分割
dst = cv2.pyrMeanShiftFiltering( img, spatialRad, colorRad, maxPyrLevel)

#图像漫水填充处理
cv2.floodFill(dst, mask, (30, 30), (0, 255, 255),
              (100, 100, 100), (50, 50, 50),
              cv2.FLOODFILL_FIXED_RANGE)

#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
