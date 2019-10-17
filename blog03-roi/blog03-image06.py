# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
test = cv2.imread("test3.jpg", cv2.IMREAD_UNCHANGED)
print test.shape

#定义300*100矩阵 3对应BGR
face = np.ones((200, 200))

#显示原始图像
cv2.imshow("Demo", img)

#显示ROI区域
face = img[100:300, 250:450]
test[200:400, 200:400] = face
cv2.imshow("Pic", test)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
