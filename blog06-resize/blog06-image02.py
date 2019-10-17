#encoding:utf-8
import cv2  
import numpy as np  
 
#读取图片
src = cv2.imread('scenery.png')
rows, cols = src.shape[:2]
print rows, cols

#图像缩放 dsize(列,行)
result = cv2.resize(src, (int(cols*0.6), int(rows*1.2)))

#显示图像
cv2.imshow("src", src)
cv2.imshow("result", result)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
