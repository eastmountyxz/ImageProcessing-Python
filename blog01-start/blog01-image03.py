# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("flower.png", cv2.IMREAD_UNCHANGED)

#该区域设置为白色
img[100:200, 150:250] = [255,255,255]

#显示图像
cv2.imshow("Demo", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像
cv2.imwrite("testyxz.jpg", img)
