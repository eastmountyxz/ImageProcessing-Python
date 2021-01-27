# -*- coding:utf-8 -*-
import cv2
import numpy

#读取图片
img = cv2.imread("Lena.png")

#获取图像形状
print(img.shape)

#获取像素数目
print(img.size)

#获取图像数据类型
print(img.dtype)
