# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib

#读取图像
img = cv2.imread('Lena.png', 0)

#傅里叶变换
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)

#将频谱低频从左上角移动至中心位置
dft_shift = np.fft.fftshift(dft)

#频谱图像双通道复数转换为0-255区间
result = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#显示图像
plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title(u'(a)原始图像'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(result, cmap = 'gray')
plt.title(u'(b)傅里叶变换处理'), plt.xticks([]), plt.yticks([])
plt.show()
