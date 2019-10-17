# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#读取图像
img = cv.imread("test06.png")
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#图像黑帽运算
kernel = np.ones((10,10), np.uint8)
result = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

#image类转numpy
imgd = np.array(result)     

#准备数据
sp = result.shape
h = int(sp[0])        #图像高度(rows)
w = int(sp[1])       #图像宽度(colums) of image

#绘图初始处理
fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection="3d")

x = np.arange(0, w, 1)
y = np.arange(0, h, 1)
x, y = np.meshgrid(x,y)
z = imgd
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  

#自定义z轴
ax.set_zlim(-10, 255)
ax.zaxis.set_major_locator(LinearLocator(10))   #设置z轴网格线的疏密
#将z的value字符串转为float并保留2位小数
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f')) 

# 设置坐标轴的label和标题
ax.set_xlabel('x', size=15)
ax.set_ylabel('y', size=15)
ax.set_zlabel('z', size=15)
ax.set_title("surface plot", weight='bold', size=20)

#添加右侧的色卡条
fig.colorbar(surf, shrink=0.6, aspect=8)  
plt.show()
