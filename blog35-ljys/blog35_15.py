#coding:utf-8
# By: Eastmount CSDN 2021-01-26
import cv2  
import numpy as np  
 
#读取图片 
img = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

#获取图像宽和高
rows, cols = img.shape[:2]
print(rows, cols)

#画圆形
circle = np.zeros((rows, cols), dtype="uint8")
cv2.circle(circle, (int(rows/2.0), int(cols/2)), 80, 255, -1)
print(circle.shape)
print(img.size, circle.size)

#OpenCV图像与运算
result = cv2.bitwise_and(img, circle)

#显示图像
cv2.imshow("original", img)
cv2.imshow("circle", circle)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
