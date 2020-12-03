# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

#读取图像
img = cv2.imread('lines.png')

#灰度变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#转换为二值图像
edges = cv2.Canny(gray, 50, 150)

#显示原始图像
plt.subplot(121), plt.imshow(edges, 'gray'), plt.title(u'(a)原始图像')
plt.axis('off')

#霍夫变换检测直线
lines = cv2.HoughLines(edges, 1, np.pi / 180, 160)

#转换为二维
line = lines[:, 0, :] 

#将检测的线在极坐标中绘制 
for rho,theta in line[:]: 
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    print(x0, y0)
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    print(x1, y1, x2, y2)
    #绘制直线
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示处理图像
plt.subplot(122), plt.imshow(img, 'gray'), plt.title(u'(b)结果图像')
plt.axis('off')
plt.show()
