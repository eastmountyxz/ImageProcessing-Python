# coding: utf-8
# 2021-05-17 Eastmount CSDN
import numpy as np
import cv2
from matplotlib import pyplot as plt

#读取原始图像
img = cv2.imread('test01.png')

#图像灰度化处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#图像阈值化处理
ret, thresh = cv2.threshold(gray, 0, 255, 
cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#显示图像
cv2.imshow('src', img)
cv2.imshow('res', thresh)
cv2.waitKey()
cv2.destroyAllWindows()
