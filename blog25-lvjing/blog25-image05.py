#coding:utf-8
import cv2
import numpy as np

#获取滤镜颜色
def getBGR(img, table, i, j):
    #获取图像颜色
    b, g, r = img[i][j]
    #计算标准颜色表中颜色的位置坐标
    x = int(g/4 + int(b/32) * 64)
    y = int(r/4 + int((b%32) / 4) * 64)
    #返回滤镜颜色表中对应的颜色
    return lj_map[x][y]

#读取原始图像
img = cv2.imread('scenery.png')
lj_map = cv2.imread('table.png')
print img.shape

#获取图像行和列
rows, cols = img.shape[:2]

#新建目标图像
dst = np.zeros((rows, cols, 3), dtype="uint8")

#循环设置滤镜颜色
for i in range(rows):
    for j in range(cols):
        dst[i][j] = getBGR(img, lj_map, i, j)
        
#显示图像
cv2.imshow('src', img)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
