# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2

#绘制曲线
def gamma_plot(c, v):
    x = np.arange(0, 256, 0.01)
    y = c*x**v
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文标签
    plt.title(u'伽马变换函数')
    plt.xlim([0, 255]), plt.ylim([0, 255])
    plt.show()

#伽玛变换
def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut) #像素灰度值的映射
    output_img = np.uint8(output_img+0.5)  
    return output_img

#读取原始图像
img = cv2.imread('2019.png')

#绘制伽玛变换曲线
gamma_plot(0.00000005, 4.0)

#图像灰度伽玛变换
output = gamma(img, 0.00000005, 4.0)

#显示图像
cv2.imshow('Imput', img)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
