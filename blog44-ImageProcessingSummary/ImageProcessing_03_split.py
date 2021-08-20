# -*- coding:utf-8 -*-
# By: Eastmount CSDN 2021-08-19
import cv2
import numpy as np

#读取图片
img = cv2.imread("Lena.png")
rows, cols, chn = img.shape
print(rows, cols, chn)
cv2.imshow("img", img)

#(1)拆分通道
b, g, r = cv2.split(img)
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)

#(2)合并通道
m = cv2.merge([b, g, r])
cv2.imshow("Merge", m)

#(3)显示蓝色通道
b_ = cv2.split(img)[0]
g_ = np.zeros((rows,cols), dtype=img.dtype) #设置g、r通道为0
r_ = np.zeros((rows,cols), dtype=img.dtype)
m = cv2.merge([b_, g_, r_])
cv2.imshow("MergeBlue", m)
cv2.imwrite("MergeBlue.png", m)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
