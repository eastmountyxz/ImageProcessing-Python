# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

#拆分通道
b = cv2.split(img)[0]
g = np.zeros((rows,cols),dtype=img.dtype)
r = np.zeros((rows,cols),dtype=img.dtype)

#合并通道
m = cv2.merge([b, g, r])
cv2.imshow("Merge", m)
           
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
