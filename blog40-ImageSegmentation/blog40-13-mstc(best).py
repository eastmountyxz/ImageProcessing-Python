# coding:utf-8
# 2021-05-17 Eastmount CSDN
import cv2
import random
import sys
import numpy as np

#使用说明 点击鼠标选择种子点
help_message = '''USAGE: floodfill.py [<image>]
Click on the image to set seed point
Keys:
  f - toggle floating range
  c - toggle 4/8 connectivity
  ESC - exit
'''
 
if __name__ == '__main__':

    #输出提示文本
    print(help_message)

    #读取原始图像
    img = cv2.imread('nv.png')

    #获取图像高和宽
    h, w = img.shape[:2]

    #设置掩码 长和宽都比输入图像多两个像素点 
    mask = np.zeros((h+2, w+2), np.uint8)

    #设置种子节点和4邻接
    seed_pt = None
    fixed_range = True
    connectivity = 4 

    #图像漫水填充分割更新函数
    def update(dummy=None):
        if seed_pt is None:
            cv2.imshow('floodfill', img)
            return
        
        #建立图像副本并漫水填充
        flooded = img.copy()
        mask[:] = 0 #掩码初始为全0
        lo = cv2.getTrackbarPos('lo', 'floodfill') #观察点像素邻域负差最大值
        hi = cv2.getTrackbarPos('hi', 'floodfill') #观察点像素邻域正差最大值
        print('lo=', lo, 'hi=', hi)

        #低位比特包含连通值 4 (缺省) 或 8
        flags = connectivity
        
        #考虑当前象素与种子象素之间的差（高比特也可以为0）
        if fixed_range:
            flags |= cv2.FLOODFILL_FIXED_RANGE
            
        #以白色进行漫水填充
        cv2.floodFill(flooded, mask, seed_pt,
                      (random.randint(0,255), random.randint(0,255),
                       random.randint(0,255)), (lo,)*3, (hi,)*3, flags)

        #选定基准点用红色圆点标出
        cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
        print("send_pt=", seed_pt)

        #显示图像
        cv2.imshow('floodfill', flooded)

    #鼠标响应函数
    def onmouse(event, x, y, flags, param):
        global seed_pt #基准点

        #鼠标左键响应选择漫水填充基准点
        if flags & cv2.EVENT_FLAG_LBUTTON:
            seed_pt = x, y
            update()

    #执行图像漫水填充分割更新操作
    update()
    
    #鼠标更新操作
    cv2.setMouseCallback('floodfill', onmouse)

    #设置进度条
    cv2.createTrackbar('lo', 'floodfill', 20, 255, update)
    cv2.createTrackbar('hi', 'floodfill', 20, 255, update)

    #按键响应操作
    while True:
        ch = 0xFF & cv2.waitKey()
        #退出
        if ch == 27:
            break
        #选定时flags的高位比特位0
        #此时邻域的选定为当前像素与相邻像素的差, 联通区域会很大
        if ch == ord('f'):
            fixed_range = not fixed_range 
            print('using %s range' % ('floating', 'fixed')[fixed_range])
            update()
        #选择4方向或则8方向种子扩散
        if ch == ord('c'):
            connectivity = 12-connectivity 
            print('connectivity =', connectivity)
            update()
    cv2.destroyAllWindows()             
