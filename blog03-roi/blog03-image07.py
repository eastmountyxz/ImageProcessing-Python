# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#拆分通道
b, g, r = cv2.split(img)

#显示原始图像
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
           
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
