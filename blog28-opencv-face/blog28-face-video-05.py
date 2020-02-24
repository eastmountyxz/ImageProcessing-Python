#coding:utf-8
import cv2
import numpy as np

# 加载视频
cap = cv2.VideoCapture('shipin01.mp4')

# 调用熟悉的人脸分类器 识别特征类型
# 人脸 - haarcascade_frontalface_default.xml
# 人眼 - haarcascade_eye.xm
# 微笑 - haarcascade_smile.xml
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # 读取视频片段
    flag, frame = cap.read()
    if flag == False:
        break

    # 灰度处理
    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)

    # 检查人脸 按照1.1倍放到 周围最小像素为5
    face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

    # 绘制矩形和圆形检测人脸
    for x, y, w, h in face_zone:
        cv2.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
        cv2.circle(frame, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

    # 显示图片
    cv2.imshow('video', frame)
    
    # 设置退出键和展示频率
    if ord('q') == cv2.waitKey(40):
        break

# 释放资源
cv2.destroyAllWindows()
cap.release()


