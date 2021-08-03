#coding:utf-8
import cv2

# 读取原始图像
img = cv2.imread("./input/person-01.png")

# 调用熟悉的人脸分类器 识别特征类型
# 人脸 - haarcascade_frontalface_default.xml
# 人眼 - haarcascade_eye.xm
# 微笑 - haarcascade_smile.xml
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 灰度处理
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

# 检查人脸 按照1.1倍放到 周围最小像素为5
face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4) # maxSize = (55,55)
print ('识别人脸的信息：\n',face_zone)

# 绘制矩形和圆形检测人脸
for x, y, w, h in face_zone:
    # 绘制矩形人脸区域
    cv2.rectangle(img, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
    # 绘制圆形人脸区域 radius表示半径
    cv2.circle(img, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

# 设置图片可以手动调节大小
cv2.namedWindow("Easmount-CSDN", 0)

# 显示图片
cv2.imshow("Easmount-CSDN", img)

# 等待显示 设置任意键退出程序
cv2.waitKey(0)
cv2.destroyAllWindows()
