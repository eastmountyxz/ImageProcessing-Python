# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-01-26
import cv2
import numpy as np

#读取图像
img = cv2.imread("Lena.png")

#显示图像
cv2.imshow("Demo", img)

#保存图像
cv2.imwrite("dst1.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])  
cv2.imwrite("dst2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  
cv2.imwrite("dst3.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])  
cv2.imwrite("dst4.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
