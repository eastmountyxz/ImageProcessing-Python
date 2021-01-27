#coding:utf-8
import cv2  
import numpy as np  
 
#读取图片 
img = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

#OpenCV图像非运算
result = cv2.bitwise_not(img)

#显示图像
cv2.imshow("original", img)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
