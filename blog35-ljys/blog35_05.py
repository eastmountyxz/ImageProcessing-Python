# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-01-26
import cv2
import numpy as np

#读取图片
img = cv2.imread("Lena.png")

#创建空图像
emptyImage = np.zeros(img.shape, np.uint8)

#复制图像
emptyImage2 = img.copy()

#显示图像
cv2.imshow("Demo1", img)
cv2.imshow("Demo2", emptyImage)
cv2.imshow("Demo3", emptyImage2)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
