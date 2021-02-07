#coding:utf-8
# By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#读取图像
src = cv2.imread('Lena.png')

#转换为RGB图像
img_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#获取BGR三个通道的像素值
b, g, r = cv2.split(src)
print(r,g,b)

plt.figure(figsize=(8, 6))

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#原始图像
plt.subplot(221)
plt.imshow(img_rgb)
plt.axis('off')
plt.title("(a)原图像")

#绘制蓝色分量直方图
plt.subplot(222)
plt.hist(b.ravel(), bins=256, density=1, facecolor='b', edgecolor='b', alpha=0.75)
plt.xlabel("x")
plt.ylabel("y")
plt.title("(b)蓝色分量直方图")

#绘制绿色分量直方图
plt.subplot(223)
plt.hist(g.ravel(), bins=256, density=1, facecolor='g', edgecolor='g', alpha=0.75)
plt.xlabel("x")
plt.ylabel("y")
plt.title("(c)绿色分量直方图")

#绘制红色分量直方图
plt.subplot(224)
plt.hist(r.ravel(), bins=256, density=1, facecolor='r', edgecolor='r', alpha=0.75)
plt.xlabel("x")
plt.ylabel("y")
plt.title("(d)红色分量直方图")
plt.show()
