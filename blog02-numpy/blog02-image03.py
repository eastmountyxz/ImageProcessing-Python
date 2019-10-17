# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#BGR图像
print(img[78, 125, 0])
print(img[78, 125, 1])
print(img[78, 125, 2])

#修改像素
img[78, 125, 0] = 255
img[78, 125, 1] = 255
img[78, 125, 2] =255

print(img[78, 125])
img[78, 125] = [10, 10, 10]
print(img[78, 125, 0])
print(img[78, 125, 1])
print(img[78, 125, 2])


#方法二
print(img[78, 125])
img[78, 125] = [10, 10, 10]
print(img[78, 125])
