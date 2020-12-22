#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np

#读取原始图像
img = cv2.imread('nv.png')

#获取图像行和列
rows, cols = img.shape[:2]

#新建目标图像
dst = np.zeros((rows, cols, 3), dtype="uint8")

#提取三个颜色通道
(b, g, r) = cv2.split(img)

#彩色图像均衡化
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

#合并通道
dst = cv2.merge((bH, gH, rH))

#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
