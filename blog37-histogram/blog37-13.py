#coding:utf-8
#By:Eastmount CSDN 2021-02-05
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#函数: 获取图像的灰度平均值
def fun_mean(img, height, width):
    sum_img = 0
    for i in range(height):
        for j in range(width):
            sum_img = sum_img + int(img[i,j])
    mean = sum_img / (height * width)
    return mean

#函数: 获取中位数
def fun_median(data):
    length = len(data)
    data.sort()
    if (length % 2)== 1: 
        z = length // 2
        y = data[z]
    else:
        y = (int(data[length//2]) + int(data[length//2-1])) / 2
    return y

#读取图像
img = cv2.imread('lena.bmp')

#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]

#计算图像的灰度平均值
mean = fun_mean(grayImage, height, width)
print("灰度平均值：", mean)

#计算图像的灰度中位数
value = grayImage.ravel() #获取所有像素值
median = fun_median(value)
print("灰度中值：", median)

#计算图像的灰度标准差
std = np.std(value, ddof = 1)
print("灰度标准差", std)
