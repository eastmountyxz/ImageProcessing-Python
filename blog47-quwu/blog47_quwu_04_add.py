import numpy as np
import cv2 as cv
import os
import random
 
file = ['fj-02.png']
output = 'fj-02-wu.png'

for file_img in file:
    #打开图像
    img = cv.imread(file_img)
    mask_img = cv.imread(file_img)
    
    #雾的颜色
    mask_img[:, :] = (166, 178, 180) 
    
    #里面参数可调，主要调整雾的浓度
    image = cv.addWeighted(img,
                           round(random.uniform(0.03, 0.28), 2),
                           mask_img, 1, 0) 

    #保存的文件夹
    cv.imwrite(output, image) 
