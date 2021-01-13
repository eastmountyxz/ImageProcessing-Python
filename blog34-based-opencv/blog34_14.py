# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((512,512,3), np.uint8)

#绘制多边形
pts = np.array([[50, 190], [380, 420], [255, 50], [120, 420], [450, 190]])
cv2.polylines(img, [pts], True, (0, 255, 255), 10)

#显示图像
cv2.imshow("ellipse", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
