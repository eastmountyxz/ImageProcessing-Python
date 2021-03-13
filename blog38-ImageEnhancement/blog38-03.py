# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-03-12
import cv2  
import numpy as np  
import matplotlib.pyplot as plt

#读取图片
img = cv2.imread('yxz.jpg')

# 彩色图像均衡化 需要分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

# 合并每一个通道
result = cv2.merge((bH, gH, rH))
cv2.imshow("Input", img)
cv2.imshow("Result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#绘制直方图
plt.figure("Hist")
#蓝色分量
plt.hist(bH.ravel(), bins=256, normed=1, facecolor='b', edgecolor='b')
#绿色分量
plt.hist(gH.ravel(), bins=256, normed=1, facecolor='g', edgecolor='g')
#红色分量
plt.hist(rH.ravel(), bins=256, normed=1, facecolor='r', edgecolor='r')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
