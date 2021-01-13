# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("Lena.png")

#显示图像
cv2.imshow("Demo", img)

#无限期等待输入
k=cv2.waitKey(0)

#如果输入ESC按键退出
if k==27:
    cv2.destroyAllWindows()
