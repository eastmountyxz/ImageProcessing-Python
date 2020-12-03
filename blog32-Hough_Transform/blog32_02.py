# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#读取图像
img = cv.imread('Na.png', 0)

#傅里叶变换
f = np.fft.fft2(img)

#转移像素做幅度普
fshift = np.fft.fftshift(f)       

#取绝对值：将复数变化成实数取对数的目的为了将数据变化到0-255
res = np.log(np.abs(fshift))

#展示结果
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(res, 'gray'), plt.title('Fourier Image')
plt.show()
