#encoding:utf-8
# By: Eastmount CSDN 2021-08-19
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
src1 = cv2.imread('lena-hd.png')
src2 = cv2.imread('na.png')
src3 = cv2.imread("Lena.png")
print(src3.shape)

#图像融合
res1 = cv2.addWeighted(src1, 0.6, src2, 0.8, 10)

#显示ROI区域
face = np.ones((100, 100, 3)) #定义150×150矩阵 3对应BGR
face = src3[200:300, 180:280]

#显示ROI区域
res3 = src2.copy()
res3[150:250, 150:250] = face

#显示图像
cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("src3", src3)
cv2.imshow("res1", res1)
cv2.imshow("res2", face)
cv2.imshow("res3", res3)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
