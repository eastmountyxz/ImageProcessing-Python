# -*- coding: utf-8 -*-
"""
2022-12-24
By: Eastmount CSDN xiuzhang
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

#-----------------------------------------------------------------------
#几何变换-镜像、翻转、旋转、缩放
def JH_Transformation(img,img_path):
    rows, cols, channel = img.shape
    #print(rows,cols,channel)
    
    #镜像处理
    jx = cv2.flip(img, 1)

    #旋转30度 (旋转中心,旋转度数,scale)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)
    rotated30 = cv2.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))

    #旋转45度 (旋转中心,旋转度数,scale)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    rotated45 = cv2.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))

    #旋转90度 (旋转中心,旋转度数,scale)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
    rotated90 = cv2.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))

    #旋转330度 (旋转中心,旋转度数,scale)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 330, 1)
    rotated330 = cv2.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))

    #旋转180度
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
    rotated180 = cv2.warpAffine(img, M, (cols, rows), borderValue=(255,255,255))

    #缩小
    sx = cv2.resize(img, (int(cols*0.8), int(rows*0.8)))
    
    #放大
    fd = cv2.resize(img, (int(cols*1.2), int(rows*1.2)))

    """
    #显示图像
    titles = ['Source', 'JX', 'XZ30', 'XZ45', 'XZ90', 'XZ330', 'XZ180', 'SX', 'FD']
    images = [img, jx, rotated30, rotated45, rotated90, rotated330, rotated180, sx, fd]
    for i in range(9):
       plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    """

    #保存图像
    cv2.imwrite(img_path[0:-4] + '_jx.png', jx)
    cv2.imwrite(img_path[0:-4] + '_rotated30.png', rotated30)
    cv2.imwrite(img_path[0:-4] + '_rotated45.png', rotated45)
    cv2.imwrite(img_path[0:-4] + '_rotated90.png', rotated90)
    cv2.imwrite(img_path[0:-4] + '_rotated330.png', rotated330)
    cv2.imwrite(img_path[0:-4] + '_rotated180.png', rotated180)
    cv2.imwrite(img_path[0:-4] + '_sx.png', sx)
    cv2.imwrite(img_path[0:-4] + '_fd.png', fd)

#-----------------------------------------------------------------------
#亮度变换-增强、减弱
def Brighter_Transformation(img, percetage):
    img_copy = img.copy()
    w = img.shape[1]
    h = img.shape[0]
    for xi in range(0, w):
        for xj in range(0, h):
            img_copy[xj, xi, 0] = np.clip(int(img[xj, xi, 0] * percetage), a_max=255, a_min=0)
            img_copy[xj, xi, 1] = np.clip(int(img[xj, xi, 1] * percetage), a_max=255, a_min=0)
            img_copy[xj, xi, 2] = np.clip(int(img[xj, xi, 2] * percetage), a_max=255, a_min=0)
    return img_copy

def Darker_Transformation(img, percetage):
    img_copy = img.copy()
    w = img.shape[1]
    h = img.shape[0]
    for xi in range(0, w):
        for xj in range(0, h):
            img_copy[xj, xi, 0] = int(img[xj, xi, 0] * percetage)
            img_copy[xj, xi, 1] = int(img[xj, xi, 1] * percetage)
            img_copy[xj, xi, 2] = int(img[xj, xi, 2] * percetage)
    return img_copy

def LD_Transformation(img,img_path):
    rows, cols, channel = img.shape
    
    #增强1.1、1.5、2.0、2.5、3.0
    zq_11 = Brighter_Transformation(img,1.1)
    zq_15 = Brighter_Transformation(img,1.5)
    zq_18 = Brighter_Transformation(img,1.8)
    zq_20 = Brighter_Transformation(img,2.0)
    zq_25 = Brighter_Transformation(img,2.5)

    #减弱0.9、0.8、0.5
    jr_09 = Darker_Transformation(img,0.9)
    jr_08 = Darker_Transformation(img,0.8)
    jr_07 = Darker_Transformation(img,0.7)

    """
    #显示图像
    titles = ['Source', 'ZQ1.1', 'ZQ1.5', 'ZQ1.8', 'ZQ2.0', 'ZQ2.5', 'JR0.9', 'JR0.8', 'JR0.7']
    images = [img, zq_11, zq_15, zq_18, zq_20, zq_25, jr_09, jr_08, jr_07]
    for i in range(9):
       plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    """
    
    #保存图像
    cv2.imwrite(img_path[0:-4] + '_zq_11.png', zq_11)
    cv2.imwrite(img_path[0:-4] + '_zq_15.png', zq_15)
    cv2.imwrite(img_path[0:-4] + '_zq_18.png', zq_18)
    cv2.imwrite(img_path[0:-4] + '_zq_20.png', zq_20)
    cv2.imwrite(img_path[0:-4] + '_zq_25.png', zq_25)
    cv2.imwrite(img_path[0:-4] + '_jr_09.png', jr_09)
    cv2.imwrite(img_path[0:-4] + '_jr_08.png', jr_08)
    cv2.imwrite(img_path[0:-4] + '_jr_07.png', jr_07)
    
#-----------------------------------------------------------------------
#颜色通道变换
def Channel_Transformation(img,img_path):
    rows, cols, channel = img.shape
    img = Brighter_Transformation(img,1.5)  #边缘增强
    color_map = [
        cv2.COLORMAP_AUTUMN,
        cv2.COLORMAP_BONE,
        cv2.COLORMAP_JET,
        cv2.COLORMAP_WINTER,
        cv2.COLORMAP_PARULA,
        cv2.COLORMAP_OCEAN,
        cv2.COLORMAP_SUMMER,
        cv2.COLORMAP_SPRING,
        cv2.COLORMAP_COOL,
        cv2.COLORMAP_PINK,
        cv2.COLORMAP_HOT,
        cv2.COLORMAP_PARULA,
        cv2.COLORMAP_MAGMA,
        cv2.COLORMAP_INFERNO,
        cv2.COLORMAP_PLASMA,
        cv2.COLORMAP_TWILIGHT,
        cv2.COLORMAP_TWILIGHT_SHIFTED
    ]

    rgb_img_01 = cv2.applyColorMap(img, color_map[0])
    rgb_img_02 = cv2.applyColorMap(img, color_map[1])
    rgb_img_03 = cv2.applyColorMap(img, color_map[9])
    rgb_img_04 = cv2.applyColorMap(img, color_map[3])
    rgb_img_05 = cv2.applyColorMap(img, color_map[13])
    rgb_img_06 = cv2.applyColorMap(img, color_map[5])
    rgb_img_07 = cv2.applyColorMap(img, color_map[12])
    rgb_img_08 = cv2.applyColorMap(img, color_map[10])

    # 通道分离
    b = cv2.split(img)[0]
    g = np.zeros((rows,cols), dtype=img.dtype)
    r = np.zeros((rows,cols), dtype=img.dtype)
    mb = cv2.merge([b, g, r])

    g = cv2.split(img)[1]
    b = np.zeros((rows,cols), dtype=img.dtype)
    r = np.zeros((rows,cols), dtype=img.dtype)
    mg = cv2.merge([b, g, r])

    r = cv2.split(img)[2]
    b = np.zeros((rows,cols), dtype=img.dtype)
    g = np.zeros((rows,cols), dtype=img.dtype)
    mr = cv2.merge([b, g, r])
    
    """
    #显示图像
    titles = ['Source', 'RGB-1', 'RGB-2', 'RGB-3', 'RGB-4',
              'RGB-5', 'RGB-6', 'RGB-7', 'RGB-8', 'B', 'G', 'R']
    images = [img, rgb_img_01, rgb_img_02, rgb_img_03, rgb_img_04,
              rgb_img_05, rgb_img_06, rgb_img_07, rgb_img_08, mb, mg, mr]
    for i in range(12):
       plt.subplot(4,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    """

    #保存图像
    cv2.imwrite(img_path[0:-4] + '_rgb_img_01.png', rgb_img_01)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_02.png', rgb_img_02)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_03.png', rgb_img_03)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_04.png', rgb_img_04)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_05.png', rgb_img_05)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_06.png', rgb_img_06)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_07.png', rgb_img_07)
    cv2.imwrite(img_path[0:-4] + '_rgb_img_08.png', rgb_img_08)
    cv2.imwrite(img_path[0:-4] + '_mb.png', mb)
    cv2.imwrite(img_path[0:-4] + '_mg.png', mg)
    cv2.imwrite(img_path[0:-4] + '_mr.png', mr)

#-----------------------------------------------------------------------
#添加高斯噪声和椒盐噪声
def GaussianNoise(img, percetage):
    gn = img.copy()
    w = img.shape[1]
    h = img.shape[0]
    G_NoiseNum = int(percetage * img.shape[0] * img.shape[1])
    for i in range(G_NoiseNum):
        lx = np.random.randint(0, h)
        ly = np.random.randint(0, w)
        gn[lx][ly][np.random.randint(3)] = np.random.randn(1)[0]
    return gn

def SaltNoise(img, percetage):
    sn = img.copy()
    SP_NoiseNum = int(percetage * img.shape[0] * img.shape[1])
    for i in range(SP_NoiseNum):
        randR = np.random.randint(0, img.shape[0] - 1)
        randG = np.random.randint(0, img.shape[1] - 1)
        randB = np.random.randint(0, 3)
        if np.random.randint(0, 1) == 0:
            sn[randR, randG, randB] = 0
        else:
            sn[randR, randG, randB] = 255
    return sn

def Gaussian_Salt_Noise(img,img_path):
    rows, cols, channel = img.shape
    img = Brighter_Transformation(img,1.5)  #边缘增强

    #高斯噪声
    gn_005 = GaussianNoise(img, 0.05)
    gn_010 = GaussianNoise(img, 0.10)
    gn_015 = GaussianNoise(img, 0.15)
    gn_020 = GaussianNoise(img, 0.20)

    #椒盐噪声
    sn_005 = SaltNoise(img, 0.05)
    sn_010 = SaltNoise(img, 0.10)
    sn_015 = SaltNoise(img, 0.15)
    sn_020 = SaltNoise(img, 0.20)

    """
    #显示图像
    titles = ['Source', 'Gaussian-0.05', 'Gaussian-0.10', 'Gaussian-0.15', 'Gaussian-0.20',
              'Salt-0.05', 'Salt-0.10', 'Salt-0.15', 'Salt-0.20']
    images = [img, gn_005, gn_010, gn_015, gn_020, sn_005, sn_010, sn_015, sn_020]
    for i in range(9):
       plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    """
    
    #保存图像
    cv2.imwrite(img_path[0:-4] + '_gn_005.png', gn_005)
    cv2.imwrite(img_path[0:-4] + '_gn_010.png', gn_010)
    cv2.imwrite(img_path[0:-4] + '_gn_015.png', gn_015)
    cv2.imwrite(img_path[0:-4] + '_gn_020.png', gn_020)
    cv2.imwrite(img_path[0:-4] + '_sn_005.png', sn_005)
    cv2.imwrite(img_path[0:-4] + '_sn_010.png', sn_010)
    cv2.imwrite(img_path[0:-4] + '_sn_015.png', sn_015)
    cv2.imwrite(img_path[0:-4] + '_sn_020.png', sn_020)

#-----------------------------------------------------------------------
#模拟怀旧和噪声添加
def Salt(img, num):
    wn = img.copy()
    rows, cols, chn = wn.shape
    for i in range(num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)    
        wn[x,y,:] = 210
    return wn

def Fog_Noise(img, percetage):
    mask_img = img.copy()
    mask_img[:, :] = (166, 178, 180)  #雾的颜色 (146,182,213)
    
    #调整雾的浓度 round(random.uniform(0.03, 0.28), 2)
    res = cv2.addWeighted(img, percetage, mask_img, 1-percetage, 0) 
    return res

def Fog_Salt_Noise(img,img_path):
    rows, cols, channel = img.shape
    img = Brighter_Transformation(img,1.5)  #边缘增强

    #白点噪声
    wn_100 = Salt(img, 100)
    wn_150 = Salt(img, 150)
    wn_200 = Salt(img, 200)
    wn_250 = Salt(img, 250)

    #模拟怀旧
    fog_06 = Fog_Noise(img, 0.6)
    fog_07 = Fog_Noise(img, 0.7)
    fog_08 = Fog_Noise(img, 0.8)
    fog_09 = Fog_Noise(img, 0.9)

    """
    #显示图像
    titles = ['Source', 'wn-100', 'wn-150', 'wn-200', 'wn-250',
              'fog_06', 'fog_07', 'fog_08', 'fog_09']
    images = [img, wn_100, wn_150, wn_200, wn_250,
              fog_06, fog_07, fog_08, fog_09]
    for i in range(9):
       plt.subplot(3,3 ,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    """

    #保存图像
    cv2.imwrite(img_path[0:-4] + '_wn_100.png', wn_100)
    cv2.imwrite(img_path[0:-4] + '_wn_150.png', wn_150)
    cv2.imwrite(img_path[0:-4] + '_wn_200.png', wn_200)
    cv2.imwrite(img_path[0:-4] + '_wn_250.png', wn_250)
    cv2.imwrite(img_path[0:-4] + '_fog_06.png', fog_06)
    cv2.imwrite(img_path[0:-4] + '_fog_07.png', fog_07)
    cv2.imwrite(img_path[0:-4] + '_fog_08.png', fog_08)
    cv2.imwrite(img_path[0:-4] + '_fog_09.png', fog_09)

#-----------------------------------------------------------------------
#读取指定文件夹下的所有图像
def main():
    file_path = "data"
    for img_name in os.listdir(file_path):
        img_path = file_path + "\\" + img_name
        res_path = "data_add" + "\\" + img_name
        img = cv2.imread(img_path)

        #1.几何变换-镜像、翻转、旋转、缩放
        JH_Transformation(img,res_path)

        #2.亮度变换-增强、减弱
        LD_Transformation(img,res_path)

        #3.颜色通道变换
        Channel_Transformation(img,res_path)

        #4.添加高斯噪声和椒盐噪声
        Gaussian_Salt_Noise(img,res_path)

        #5.模拟怀旧和噪声添加
        Fog_Salt_Noise(img,res_path)
        
if __name__ == "__main__":
    main()

