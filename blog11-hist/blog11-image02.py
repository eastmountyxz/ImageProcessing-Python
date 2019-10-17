#encoding:utf-8
import cv2  
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('Lena.png')
#参数:原图像 通道[0]-B 掩码 BINS为256 像素范围0-255 
hist = cv2.calcHist([src], [0], None, [256], [0,255])
print(type(hist))
print(hist.size)
print(hist.shape)
print(hist)
