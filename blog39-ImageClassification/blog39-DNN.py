# -*- coding: utf-8 -*-
# By: Eastmount CSDN 2021-04-01
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

#----------------------------------------------------------------------------------
# 第一步 图像读取及转换为像素直方图
#----------------------------------------------------------------------------------

X = []
Y = []

for i in range(0, 10):
    #遍历文件夹，读取图片
    for f in os.listdir("photo/%s" % i):
        #获取图像像素
        Images = cv2.imread("photo/%s/%s" % (i, f)) 
        image=cv2.resize(Images,(256,256),interpolation=cv2.INTER_CUBIC)
        hist = cv2.calcHist([image], [0,1], None, [256,256], [0.0,255.0,0.0,255.0]) 
        X.append((hist/255).flatten())
        Y.append(i)
        
X = np.array(X)
Y = np.array(Y)

#切分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.3, random_state=1)

#----------------------------------------------------------------------------------
# 第二步 定义神经网络函数
#----------------------------------------------------------------------------------

from sklearn.preprocessing import LabelBinarizer
import random

def logistic(x):
    return 1 / (1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))

class NeuralNetwork:
    def predict(self, x):
        for b, w in zip(self.biases, self.weights):
            # 计算权重相加再加上偏向的结果
            z = np.dot(x, w) + b
            # 计算输出值
            x = self.activation(z)
        return self.classes_[np.argmax(x, axis=1)]
    
class BP(NeuralNetwork):
    
    def __init__(self,layers,batch):
                
        self.layers = layers
        self.batch = batch
        self.activation = logistic
        self.activation_deriv = logistic_derivative
        
        self.num_layers = len(layers)
        self.biases = [np.random.randn(x) for x in layers[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(layers[:-1], layers[1:])]
        
    def fit(self, X, y, learning_rate=0.1, epochs=1):
    
        labelbin = LabelBinarizer()
        y = labelbin.fit_transform(y)
        self.classes_ = labelbin.classes_
        training_data = [(x,y) for x, y in zip(X, y)]
        n = len(training_data)
        for k in range(epochs):
        #每次迭代都循环一次训练
            #训练集乱序
            random.shuffle(training_data)
            batches = [training_data[k:k+self.batch] for k in range(0, n, self.batch)]
            #批量梯度下降
            for mini_batch in batches:
                x = []
                y = []
                for a,b in mini_batch:
                    x.append(a)
                    y.append(b)
                activations = [np.array(x)]
                #向前一层一层的走
                for b, w in zip(self.biases, self.weights):
                    #计算激活函数的参数,计算公式：权重.dot(输入)+偏向 
                    z = np.dot(activations[-1],w)+b 
                    #计算输出值
                    output = self.activation(z)
                    #将本次输出放进输入列表 后面更新权重的时候备用
                    activations.append(output)
                #计算误差值
                error = activations[-1]-np.array(y)
                #计算输出层误差率
                deltas = [error * self.activation_deriv(activations[-1])]
                
                #循环计算隐藏层的误差率 从倒数第2层开始
                for l in range(self.num_layers-2, 0, -1):
                    deltas.append(self.activation_deriv(activations[l]) * np.dot(deltas[-1],self.weights[l].T))

                #将各层误差率顺序颠倒 准备逐层更新权重和偏向
                deltas.reverse()
                #更新权重和偏向
                for j in range(self.num_layers-1):
                    # 权重的增长量 计算公式为: 增长量 = 学习率 × (错误率.dot(输出值))
                    delta = learning_rate/self.batch*((np.atleast_2d(activations[j].sum(axis=0)).T).dot(np.atleast_2d(deltas[j].sum(axis=0))))
                    #更新权重
                    self.weights[j] -= delta
                    #偏向增加量 计算公式为: 学习率 × 错误率
                    delta = learning_rate/self.batch * deltas[j].sum(axis=0)
                    #更新偏向
                    self.biases[j] -= delta
        return self   

#----------------------------------------------------------------------------------
# 第三步 基于神经网络的图像分类处理
#----------------------------------------------------------------------------------

clf = BP([X_train.shape[1],10],10).fit(X_train,y_train,epochs=100)
predictions_labels = clf.predict(X_test)
print('预测结果:')
print(predictions_labels)
print('算法评价:')
print(classification_report(y_test, predictions_labels))
