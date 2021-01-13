# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((256,256,3), np.uint8)

#绘制圆形
cv2.circle(img, (100,100), 50, (255,255,0), 4)

#显示图像
cv2.imshow("circle", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
