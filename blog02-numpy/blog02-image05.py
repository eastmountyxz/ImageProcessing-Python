# -*- coding:utf-8 -*-
import cv2
import numpy

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#Numpy读取像素
blue = img.item(78, 100, 0)
green = img.item(78, 100, 1)
red = img.item(78, 100, 2)
print(blue)
print(green)
print(red)

#显示图像
cv2.imshow("Demo", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
