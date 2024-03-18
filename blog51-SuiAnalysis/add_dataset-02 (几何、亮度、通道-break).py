# -*- coding: utf-8 -*-
"""
2022-12-24
By: Eastmount CSDN xiuzhang
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
    
    #显示图像
    titles = ['Source', 'JX', 'XZ30', 'XZ45', 'XZ90', 'XZ330', 'XZ180', 'SX', 'FD']
    images = [img, jx, rotated30, rotated45, rotated90, rotated330, rotated180, sx, fd]
    for i in range(9):
       plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()

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

#亮度变换-增强、减弱
def LD_Transformation(img,img_path):
    rows, cols, channel = img.shape
    
    #增强1.1、1.5、2.0、2.5、3.0
    zq_11 = Brighter_Transformation(img,1.1)
    zq_15 = Brighter_Transformation(img,1.5)
    zq_20 = Brighter_Transformation(img,2.0)
    zq_25 = Brighter_Transformation(img,2.5)
    zq_30 = Brighter_Transformation(img,3.0)

    #减弱0.9、0.8、0.5
    jr_09 = Darker_Transformation(img,0.9)
    jr_08 = Darker_Transformation(img,0.8)
    jr_07 = Darker_Transformation(img,0.7)

    #显示图像
    titles = ['Source', 'ZQ1.1', 'ZQ1.5', 'ZQ2.0', 'ZQ2.5', 'ZQ3.0', 'JR0.9', 'JR0.8', 'JR0.7']
    images = [img, zq_11, zq_15, zq_20, zq_25, zq_30, jr_09, jr_08, jr_07]
    for i in range(9):
       plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()

    #保存图像
    cv2.imwrite(img_path[0:-4] + '_zq_11.png', zq_11)
    cv2.imwrite(img_path[0:-4] + '_zq_15.png', zq_15)
    cv2.imwrite(img_path[0:-4] + '_zq_20.png', zq_20)
    cv2.imwrite(img_path[0:-4] + '_zq_25.png', zq_25)
    cv2.imwrite(img_path[0:-4] + '_zq_30.png', zq_30)
    cv2.imwrite(img_path[0:-4] + '_jr_09.png', jr_09)
    cv2.imwrite(img_path[0:-4] + '_jr_08.png', jr_08)
    cv2.imwrite(img_path[0:-4] + '_jr_07.png', jr_07)
    
#-----------------------------------------------------------------------
#颜色通道变换
def Channel__Transformation(img,img_path):
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
#读取指定文件夹下的所有图像
def main():
    file_path = "data"
    for img_name in os.listdir(file_path):
        img_path = file_path + "\\" + img_name
        img = cv2.imread(img_path)

        #1.几何变换-镜像、翻转、旋转、缩放
        JH_Transformation(img,img_path)

        #2.亮度变换-增强、减弱
        LD_Transformation(img,img_path)

        #3.颜色通道变换
        Channel__Transformation(img,img_path)
        

        break
        
if __name__ == "__main__":
    main()

