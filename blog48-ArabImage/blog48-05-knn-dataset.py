# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:54:36 2021
@author: xiuzhang CSDN
参考：刘润森老师博客 推荐大家关注 很厉害的一位CV大佬
     https://maoli.blog.csdn.net/article/details/117688738
"""
import numpy as np
import pandas as pd
from IPython.display import display
import csv
from PIL import Image
from scipy.ndimage import rotate

#----------------------------------------------------------------
#                      第一步 读取数据
#----------------------------------------------------------------
#训练数据images和labels
letters_training_images_file_path = "dataset/csvTrainImages 13440x1024.csv"
letters_training_labels_file_path = "dataset/csvTrainLabel 13440x1.csv"
#测试数据images和labels
letters_testing_images_file_path = "dataset/csvTestImages 3360x1024.csv"
letters_testing_labels_file_path = "dataset/csvTestLabel 3360x1.csv"

#加载数据
training_letters_images = pd.read_csv(letters_training_images_file_path, header=None)
training_letters_labels = pd.read_csv(letters_training_labels_file_path, header=None)
testing_letters_images = pd.read_csv(letters_testing_images_file_path, header=None)
testing_letters_labels = pd.read_csv(letters_testing_labels_file_path, header=None)
print("%d个32x32像素的训练阿拉伯字母图像" % training_letters_images.shape[0])
print("%d个32x32像素的测试阿拉伯字母图像" % testing_letters_images.shape[0])
print(training_letters_images.head())
print(np.unique(training_letters_labels))


#----------------------------------------------------------------
#                      第二步 数值转换为图像特征
#----------------------------------------------------------------
#原始数据集被反射使用np.flip翻转它 通过rotate旋转从而获得更好的图像
def convert_values_to_image(image_values, display=False):
    #转换成32x32
    image_array = np.asarray(image_values)
    image_array = image_array.reshape(32,32).astype('uint8')
    #翻转+旋转
    image_array = np.flip(image_array, 0)
    image_array = rotate(image_array, -90)
    #图像显示
    new_image = Image.fromarray(image_array)
    if display == True:
        new_image.show()
    return new_image

#convert_values_to_image(training_letters_images.loc[0], True)


#----------------------------------------------------------------
#                      第三步 图像标准化处理
#----------------------------------------------------------------
training_letters_images_scaled = training_letters_images.values.astype('float32')/255
training_letters_labels = training_letters_labels.values.astype('int32')
testing_letters_images_scaled = testing_letters_images.values.astype('float32')/255
testing_letters_labels = testing_letters_labels.values.astype('int32')
print("Training images of letters after scaling")
print(training_letters_images_scaled.shape)
print(training_letters_images_scaled[0:5])


#----------------------------------------------------------------
#                      第四步 输出One-hot编码转换
#----------------------------------------------------------------
import keras
from numpy import *
from keras.utils import to_categorical
number_of_classes = 28
training_letters_labels_encoded = to_categorical(training_letters_labels-1, 
                                                 num_classes=number_of_classes)
testing_letters_labels_encoded = to_categorical(testing_letters_labels-1, 
                                                num_classes=number_of_classes)
print(training_letters_labels)
print(training_letters_labels_encoded)
print(training_letters_images_scaled.shape)
# (13440, 1024)

#机器学习不使用One-hot 每个值减1处理
training_letters_labels_list = training_letters_labels.tolist()
testing_letters_labels_list = testing_letters_labels.tolist()
print(training_letters_labels_list[:10])
#[[1], [1], [1], [1], [1], [1], [1], [1], [2], [2]]

training_letters_labels_res = [i-1 for num in training_letters_labels_list for i in num]
testing_letters_labels_res = [i-1 for num in testing_letters_labels_list for i in num]
print(training_letters_labels_res[:10])
print(len(training_letters_labels_res), len(testing_letters_labels_res))
#[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]


#----------------------------------------------------------------
#                         第五步 形状修改
#----------------------------------------------------------------
#输入形状 32x32x1 注意sklearn.fit接收两维否则报错
#ValueError: Found array with dim 4. Estimator expected <= 2.
training_letters_images_scaled = training_letters_images_scaled.reshape([-1, 32*32*1])
testing_letters_images_scaled = testing_letters_images_scaled.reshape([-1, 32*32*1])
print(training_letters_images_scaled.shape, 
      training_letters_labels_encoded.shape, 
      testing_letters_images_scaled.shape, 
      testing_letters_labels_encoded.shape)
# (13440, 32, 32, 1) (13440, 28) (3360, 32, 32, 1) (3360, 28)
# (13440, 1024) (13440, 28) (3360, 1024) (3360, 28)


#----------------------------------------------------------------
#                         第六步 KNN模型设计
#----------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC  
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, classification_report

#clf = KNeighborsClassifier(n_neighbors=11)
#clf = BernoulliNB()
#clf = SVC()
#clf = DecisionTreeClassifier(criterion='gini',max_depth=4,random_state=1)
#clf = LogisticRegression(C=100.0,random_state=1)
clf = RandomForestClassifier(n_estimators=25,random_state=1,n_jobs=2,verbose=1)
#clf = AdaBoostClassifier()

clf.fit(training_letters_images_scaled, training_letters_labels_res)
predictions_labels = clf.predict(testing_letters_images_scaled)

print('预测结果:')
print(predictions_labels)
print(testing_letters_labels_res)

print('算法评价:')
print((classification_report(testing_letters_labels_res, 
                             predictions_labels,
                             digits=4)))
