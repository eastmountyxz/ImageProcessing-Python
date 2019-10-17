# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("flower.png", cv2.IMREAD_UNCHANGED)
test = img[88,142]
print test

img[88,142] = [255, 255, 255]
print test

#分别获取BGR通道像素
blue = img[88,142,0]
print blue
green = img[88,142,1]
print green
red = img[88,142,2]
print red

#显示图像
cv2.imshow("Demo", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像
cv2.imwrite("testyxz.jpg", img)
