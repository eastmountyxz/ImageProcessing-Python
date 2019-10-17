#coding:utf-8
import cv2
import math
import numpy as np

#读取原始图像
img = cv2.imread('scenery.png')

#获取图像行和列
rows, cols = img.shape[:2]

#设置中心点
centerX = rows / 2
centerY = cols / 2
print centerX, centerY
radius = min(centerX, centerY)
print radius

#设置光照强度
strength = 200

#新建目标图像
dst = np.zeros((rows, cols, 3), dtype="uint8")

#图像光照特效
for i in range(rows):
    for j in range(cols):
        #计算当前点到光照中心距离(平面坐标系中两点之间的距离)
        distance = math.pow((centerY-j), 2) + math.pow((centerX-i), 2)
        #获取原始图像
        B =  img[i,j][0]
        G =  img[i,j][1]
        R = img[i,j][2]
        if (distance < radius * radius):
            #按照距离大小计算增强的光照值
            result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))
            B = img[i,j][0] + result
            G = img[i,j][1] + result
            R = img[i,j][2] + result
            #判断边界 防止越界
            B = min(255, max(0, B))
            G = min(255, max(0, G))
            R = min(255, max(0, R))
            dst[i,j] = np.uint8((B, G, R))
        else:
            dst[i,j] = np.uint8((B, G, R))
        
#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
