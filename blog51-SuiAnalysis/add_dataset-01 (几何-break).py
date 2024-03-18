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
#读取指定文件夹下的所有图像
def main():
    file_path = "data"
    for img_name in os.listdir(file_path):
        img_path = file_path + "\\" + img_name
        img = cv2.imread(img_path)

        #1.几何变换-镜像、翻转、旋转、缩放
        JH_Transformation(img,img_path)

        break
        
if __name__ == "__main__":
    main()

