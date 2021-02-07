#coding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#读取图像
img = cv2.imread('yxz.png')

#转换为RGB图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#设置掩膜
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:300] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)

#图像直方图计算
hist_full = cv2.calcHist([img], [0], None, [256], [0,256]) #通道[0]-灰度图

#图像直方图计算(含掩膜)
hist_mask = cv2.calcHist([img], [0], mask, [256], [0,256])

plt.figure(figsize=(8, 6))

#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

#原始图像
plt.subplot(221)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title("(a)原始图像")

#绘制掩膜
plt.subplot(222)
plt.imshow(mask, 'gray')
plt.axis('off')
plt.title("(b)掩膜")

#绘制掩膜设置后的图像
plt.subplot(223)
plt.imshow(masked_img, 'gray')
plt.axis('off')
plt.title("(c)图像掩膜处理")

#绘制直方图
plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.title("(d)直方图曲线")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
