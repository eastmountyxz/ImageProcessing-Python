#encoding:utf-8
import cv2  
import numpy as np  

#读取图片
src = cv2.imread('miao.jpg')

#灰度图像处理
GrayImage = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#二进制阈值化处理
r, b = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY)
print(r)

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", b)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
