# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

#读取图像
img = cv.imread('test.png', 0)

#快速傅里叶变换算法得到频率分布
f = np.fft.fft2(img)

#默认结果中心点位置是在左上角,
#调用fftshift()函数转移到中间位置
fshift = np.fft.fftshift(f)       

#fft结果是复数, 其绝对值结果是振幅
fimg = np.log(np.abs(fshift))

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#展示结果
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('(a)原始图像')
plt.axis('off')
plt.subplot(122), plt.imshow(fimg, 'gray'), plt.title('(b)傅里叶变换处理')
plt.axis('off')
plt.show()
