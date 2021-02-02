#encoding:utf-8
#By:Eastmount CSDN 2021-02-01
import cv2
import numpy as np

#读取图片
src = cv2.imread('test.bmp')

#图像平移矩阵
M = np.float32([[1, 0, 100], [0, 1, 50]])

#获取原始图像列数和行数
rows, cols = src.shape[:2]

#图像平移
result = cv2.warpAffine(src, M, (cols, rows)) 

#显示图像
cv2.imshow("original", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

