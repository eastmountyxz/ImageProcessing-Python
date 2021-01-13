# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((256,256,3), np.uint8)

#绘制直线
cv2.line(img, (0,0), (255,255), (55,255,155), 5)

#显示图像
cv2.imshow("line", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
