# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-01-26
import cv2
import numpy

#读取图片
img = cv2.imread("Lena.png")

#拆分通道
b, g, r = cv2.split(img)

#b = img[:, :, 0]
#g = img[:, :, 1]
#r = img[:, :, 2]

#显示原始图像
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
