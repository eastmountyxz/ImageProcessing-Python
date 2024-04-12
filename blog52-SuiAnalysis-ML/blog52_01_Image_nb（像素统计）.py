# -*- coding: utf-8 -*-
"""
By: Eastmount CSDN xiuzhang 2024-04-12
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

#-----------------------------------------------------------------------
#第一步 读取数据集并划分训练集
X = [] #定义图像名称
Y = [] #定义图像分类类标
Z = [] #定义图像像素

#遍历文件夹读取图片
for i in range(0, 12):
    for f in os.listdir("final_data/%s" % i):
        X.append("final_data//" +str(i) + "//" + str(f))
        Y.append(i)
X = np.array(X)
Y = np.array(Y)
print(X[:2])

X_train, X_test, y_train, y_test = train_test_split(X, Y,                                                   
test_size=0.3, random_state=1)
print(len(X_train), len(X_test), len(y_train), len(y_test))
#3696 1584 3696 1584

#-----------------------------------------------------------------------
#第二步 图像读取及转换为像素直方图
#训练集
XX_train = []
for i in X_train:
    image = cv2.imread(i)
    img = cv2.resize(image, (32,32),
                     interpolation=cv2.INTER_CUBIC)
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])
    XX_train.append(((hist/255).flatten()))

#测试集
XX_test = []
for i in X_test:
    image = cv2.imread(i)
    img = cv2.resize(image, (32,32),
                     interpolation=cv2.INTER_CUBIC)
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])
    XX_test.append(((hist/255).flatten()))

#-----------------------------------------------------------------------
#第三步 基于机器学习的图像分类处理
clf = BernoulliNB().fit(XX_train, y_train)
predictions_labels = clf.predict(XX_test)
print('预测结果:')
print(predictions_labels)
print('算法评价:')
print(classification_report(y_test, predictions_labels,digits=4))

#输出前10张图片及预测结果
k = 0
while k<10:
    print(X_test[k])
    image = cv2.imread(X_test[k])
    print(predictions_labels[k])
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    k = k + 1
