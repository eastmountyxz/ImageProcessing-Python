#coding:utf-8
# 2021-05-17 Eastmount CSDN
import cv2
import numpy as np

#读取原始图像
img = cv2.imread('test.png')

#获取图像行和列
rows, cols = img.shape[:2]

#目标图像
dst = img.copy()

#mask必须行和列都加2且必须为uint8单通道阵列
#mask多出来的2可以保证扫描的边界上的像素都会被处理
mask = np.zeros([rows+2, cols+2], np.uint8)  

#图像漫水填充处理
#种子点位置(30,30) 设置颜色(0,255,255) 连通区范围设定loDiff upDiff
#src(seed.x, seed.y) - loDiff <= src(x, y) <= src(seed.x, seed.y) +upDiff
cv2.floodFill(dst, mask, (30, 30), (0, 255, 255),
              (100, 100, 100), (50, 50, 50),
              cv2.FLOODFILL_FIXED_RANGE)

#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
