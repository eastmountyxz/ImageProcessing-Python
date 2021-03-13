# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-03-12
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('test.png')

#灰度转换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#直方图均衡化处理
result = cv2.equalizeHist(gray)

#显示图像
cv2.imshow("Input", gray)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

