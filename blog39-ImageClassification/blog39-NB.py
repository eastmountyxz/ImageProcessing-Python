# -*- coding: utf-8 -*-
# By: Eastmount CSDN 2021-04-01
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

#----------------------------------------------------------------------------------
# 第一步 切分训练集和测试集
#----------------------------------------------------------------------------------

X = [] #定义图像名称
Y = [] #定义图像分类类标
Z = [] #定义图像像素

for i in range(0, 10):
    #遍历文件夹，读取图片
    for f in os.listdir("photo/%s" % i):
        #获取图像名称
        X.append("photo//" +str(i) + "//" + str(f))
        #获取图像类标即为文件夹名称
        Y.append(i)

X = np.array(X)
Y = np.array(Y)

#随机率为100% 选取其中的30%作为测试集
X_train, X_test, y_train, y_test = train_test_split(X, Y,                                                   
test_size=0.3, random_state=1)

print(len(X_train), len(X_test), len(y_train), len(y_test))

#----------------------------------------------------------------------------------
# 第二步 图像读取及转换为像素直方图
#----------------------------------------------------------------------------------

#训练集
XX_train = []
for i in X_train:
    #读取图像
    #print i
    image = cv2.imread(i)
    
    #图像像素大小一致
    img = cv2.resize(image, (256,256),
                     interpolation=cv2.INTER_CUBIC)

    #计算图像直方图并存储至X数组
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])

    XX_train.append(((hist/255).flatten()))

#测试集
XX_test = []
for i in X_test:
    #读取图像
    #print i
    image = cv2.imread(i)
    
    #图像像素大小一致
    img = cv2.resize(image, (256,256),
                     interpolation=cv2.INTER_CUBIC)

    #计算图像直方图并存储至X数组
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])

    XX_test.append(((hist/255).flatten()))

#----------------------------------------------------------------------------------
# 第三步 基于朴素贝叶斯的图像分类处理
#----------------------------------------------------------------------------------

from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB().fit(XX_train, y_train)
predictions_labels = clf.predict(XX_test)

print('预测结果:')
print(predictions_labels)

print('算法评价:')
print(classification_report(y_test, predictions_labels))

#输出前10张图片及预测结果
k = 0
while k<10:
    #读取图像
    print(X_test[k])
    image = cv2.imread(X_test[k])
    print(predictions_labels[k])
    #显示图像
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    k = k + 1
