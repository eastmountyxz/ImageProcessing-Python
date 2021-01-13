# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((256,256,3), np.uint8)

#绘制矩形
cv2.rectangle(img, (20,20), (150,250), (255,0,0), 2)

#显示图像
cv2.imshow("rectangle", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
