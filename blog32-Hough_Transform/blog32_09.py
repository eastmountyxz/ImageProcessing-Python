# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

#读取图像
img = cv2.imread('judge.png')

#灰度转换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#转换为二值图像
edges = cv2.Canny(gray, 50, 200)

#显示原始图像
plt.subplot(121), plt.imshow(edges, 'gray'), plt.title(u'(a)原始图像')
plt.axis('off')

#霍夫变换检测直线
minLineLength = 60
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, minLineLength, maxLineGap)

#绘制直线
lines1 = lines[:, 0, :]
for x1,y1,x2,y2 in lines1[:]:
    cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 2)

res = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示处理图像
plt.subplot(122), plt.imshow(res), plt.title(u'(b)结果图像')
plt.axis('off')
plt.show()
