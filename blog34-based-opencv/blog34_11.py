# -*- coding:utf-8 -*-
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((256,256,3), np.uint8)

#绘制椭圆
#椭圆中心(120,100) 长轴和短轴为(100,50)
#偏转角度为20
#圆弧起始角的角度0 圆弧终结角的角度360
#颜色(255,0,255) 线条粗细2
cv2.ellipse(img, (120, 100), (100, 50), 20, 0, 360, (255, 0, 255), 2)

#显示图像
cv2.imshow("ellipse", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
