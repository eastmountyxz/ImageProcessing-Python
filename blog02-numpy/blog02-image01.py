# -*- coding:utf-8 -*-
import cv2

#读取图片
img = cv2.imread("picture.bmp", cv2.IMREAD_UNCHANGED)

#灰度图像
p = img[88, 142]
print(p)

#显示图像
cv2.imshow("Demo", img)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像
cv2.imwrite("testyxz.jpg", img)
