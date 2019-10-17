# -*- coding:utf-8 -*-
import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

#加噪声
for i in range(5000):    
    x = np.random.randint(0, rows) 
    y = np.random.randint(0, cols)    
    img[x,y,:] = 255

cv2.imshow("noise", img)
           
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
