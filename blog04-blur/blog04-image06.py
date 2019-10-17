#encoding:utf-8
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
 
#读取图片
img = cv2.imread('test01.jpg')
 
#高斯滤波
result = cv2.medianBlur(img, 3)

#显示图像
cv2.imshow("source img", img)
cv2.imshow("medianBlur", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
