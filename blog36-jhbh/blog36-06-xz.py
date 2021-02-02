#encoding:utf-8
#By:Eastmount CSDN 2021-02-01
import cv2  
import numpy as np  
 
#读取图片
src = cv2.imread('test.bmp')

#源图像的高、宽 以及通道数
rows, cols, channel = src.shape

#绕图像的中心旋转
M = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1) #旋转中心 旋转度数 scale
rotated = cv2.warpAffine(src, M, (cols, rows))  #原始图像 旋转参数 元素图像宽高

#显示图像
cv2.imshow("src", src)
cv2.imshow("rotated", rotated)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
