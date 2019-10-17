# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#定义300*100矩阵 3对应BGR
face = np.ones((200, 200, 3))

#显示原始图像
cv2.imshow("Demo", img)

#显示ROI区域
face = img[100:300, 250:450]
img[0:200,0:200] = face
cv2.imshow("face", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
