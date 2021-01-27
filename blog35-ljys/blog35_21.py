# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-01-26
import cv2
import numpy as np

#读取图片
img = cv2.imread("Lena.png")
test = cv2.imread("test.jpg")

#定义150×150矩阵 3对应BGR
face = np.ones((150, 150, 3))

#显示ROI区域
face = img[170:320, 170:320]
cv2.imshow("Demo", face)

test[220:370, 220:370] = face
cv2.imshow("Result", test)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
