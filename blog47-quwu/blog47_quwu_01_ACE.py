# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-03-12
# 惨zmshy2128老师文章并修改成Python3代码
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

#线性拉伸处理
#去掉最大最小0.5%的像素值 线性拉伸至[0,1]
def stretchImage(data, s=0.005, bins = 2000):   
    ht = np.histogram(data, bins);
    d = np.cumsum(ht[0])/float(data.size)
    lmin = 0; lmax=bins-1
    while lmin<bins:
        if d[lmin]>=s:
            break
        lmin+=1
    while lmax>=0:
        if d[lmax]<=1-s:
            break
        lmax-=1
    return np.clip((data-ht[1][lmin])/(ht[1][lmax]-ht[1][lmin]), 0,1)

#根据半径计算权重参数矩阵
g_para = {}
def getPara(radius = 5):                        
    global g_para
    m = g_para.get(radius, None)
    if m is not None:
        return m
    size = radius*2+1
    m = np.zeros((size, size))
    for h in range(-radius, radius+1):
        for w in range(-radius, radius+1):
            if h==0 and w==0:
                continue
            m[radius+h, radius+w] = 1.0/math.sqrt(h**2+w**2)
    m /= m.sum()
    g_para[radius] = m
    return m

#常规的ACE实现
def zmIce(I, ratio=4, radius=300):                     
    para = getPara(radius)
    height,width = I.shape
    zh = []
    zw = []
    n = 0
    while n < radius:
        zh.append(0)
        zw.append(0)
        n += 1
    for n in range(height):
        zh.append(n)
    for n in range(width):
        zw.append(n)
    n = 0
    while n < radius:
        zh.append(height-1)
        zw.append(width-1)
        n += 1
    #print(zh)
    #print(zw)
    
    Z = I[np.ix_(zh, zw)]
    res = np.zeros(I.shape)
    for h in range(radius*2+1):
        for w in range(radius*2+1):
            if para[h][w] == 0:
                continue
            res += (para[h][w] * np.clip((I-Z[h:h+height, w:w+width])*ratio, -1, 1))
    return res

#单通道ACE快速增强实现
def zmIceFast(I, ratio, radius):
    print(I)
    height, width = I.shape[:2]
    if min(height, width) <=2:
        return np.zeros(I.shape)+0.5
    Rs = cv2.resize(I, (int((width+1)/2), int((height+1)/2)))
    Rf = zmIceFast(Rs, ratio, radius)             #递归调用
    Rf = cv2.resize(Rf, (width, height))
    Rs = cv2.resize(Rs, (width, height))
 
    return Rf+zmIce(I,ratio, radius)-zmIce(Rs,ratio,radius)   

#rgb三通道分别增强 ratio是对比度增强因子 radius是卷积模板半径          
def zmIceColor(I, ratio=4, radius=3):               
    res = np.zeros(I.shape)
    for k in range(3):
        res[:,:,k] = stretchImage(zmIceFast(I[:,:,k], ratio, radius))
    return res

#主函数
if __name__ == '__main__':
    img = cv2.imread('car-01.png')
    res = zmIceColor(img/255.0)*255
    cv2.imwrite('car-02-Ice.jpg', res)
