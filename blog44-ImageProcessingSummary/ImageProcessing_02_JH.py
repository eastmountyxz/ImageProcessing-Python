# -*- coding: utf-8 -*-
# By:Eastmount CSDN
import cv2
import numpy as np

#创建黑色图像
img = np.zeros((512,512,3), np.uint8)

#(1)绘制直线：图像、起点坐标、终点坐标、颜色、粗细
cv2.line(img, (0,0), (512,512), (55,255,155), 5)

#(2)绘制矩形：图像、左上角坐标、右下角坐标、颜色、粗细
cv2.rectangle(img, (20,300), (350,450), (255,0,0), 2)

#(3)绘制圆形：图像、圆心坐标、半径、颜色、粗细\填充
cv2.circle(img, (400,400), 50, (255,255,0), -1)

#(4)绘制椭圆：图像、圆心坐标、长轴和短轴、偏转角度20
# 圆弧起始角的角度、圆弧终结角的角度、颜色、线条粗细
cv2.ellipse(img, (320, 100), (100, 50), 20, 0, 360, (255, 0, 255), 2)

#(5)绘制多边形：图像、多边形曲线阵列、是否闭合、颜色、粗细
pts = np.array([[10,80], [120,80], [120,200], [30,250]])
cv2.polylines(img, [pts], True, (255, 255, 255), 5)

#(6)绘制多边形
pts = np.array([[50, 190], [380, 420], [255, 50], [120, 420], [450, 190]])
cv2.polylines(img, [pts], True, (0, 255, 255), 1)

#(7)绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'I love Python!!! By:Eatmount CSDN',
            (10, 500), font, 0.6, (255, 255, 0), 2)

#显示图像
cv2.imshow("img", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
