# -*- coding: utf-8 -*-
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('people.png')

#图像向下取样
r1 = cv2.pyrDown(img)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)

#显示图像
cv2.imshow('original', img)
cv2.imshow('PyrDown1', r1)
cv2.imshow('PyrDown2', r2)
cv2.imshow('PyrDown3', r3)
cv2.waitKey()
cv2.destroyAllWindows()
