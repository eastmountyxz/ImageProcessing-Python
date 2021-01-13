# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((256,256,3), np.uint8)

#绘制多边形
pts = np.array([[10,80], [120,80], [120,200], [30,250]])
cv2.polylines(img, [pts], True, (255, 255, 255), 5)

#显示图像
cv2.imshow("ellipse", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
