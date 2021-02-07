#encoding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#函数: 判断黑夜或白天
def func_judge(img):
    #获取图像高度和宽度
    height = grayImage.shape[0]
    width = grayImage.shape[1]
    piexs_sum = height * width
    dark_sum = 0  #偏暗像素个数
    dark_prop = 0 #偏暗像素所占比例
    
    for i in range(height):
        for j in range(width):
            if img[i, j] < 50: #阈值为50
                dark_sum += 1

    #计算比例
    print(dark_sum)
    print(piexs_sum)
    dark_prop = dark_sum * 1.0 / piexs_sum 
    if dark_prop >=0.8:
        print("This picture is dark!", dark_prop)
    else:
        print("This picture is bright!", dark_prop)
               
#读取图像
img = cv2.imread('day.png')

#转换为RGB图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#计算256灰度级的图像直方图
hist = cv2.calcHist([grayImage], [0], None, [256], [0,255])

#判断黑夜或白天
func_judge(grayImage)

#显示原始图像和绘制的直方图
plt.subplot(121), plt.imshow(img_rgb, 'gray'), plt.axis('off'), plt.title("(a)")
plt.subplot(122), plt.plot(hist, color='r'), plt.xlabel("x"), plt.ylabel("y"), plt.title("(b)")
plt.show()
