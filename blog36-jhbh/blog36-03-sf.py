#encoding:utf-8
#By:Eastmount CSDN 2021-02-01
import cv2  
import numpy as np  
 
#读取图片
src = cv2.imread('test.bmp')

#图像缩放
result = cv2.resize(src, (200,100))
print(result.shape)

#显示图像
cv2.imshow("original", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
