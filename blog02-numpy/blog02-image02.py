# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#BGR图像
b = img[78, 125, 0]
print(b)
g = img[78, 125, 1]
print(g)
r = img[78, 125, 2]
print(r)

#方法二
bgr = img[78, 125]
print(bgr)

#显示图像
cv2.imshow("Demo", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像
cv2.imwrite("testyxz.jpg", img)
