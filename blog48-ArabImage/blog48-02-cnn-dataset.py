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

convert_values_to_image(training_letters_images.loc[0], True)


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


#----------------------------------------------------------------
#                         第五步 形状修改
#----------------------------------------------------------------
#输入形状 32x32x1
training_letters_images_scaled = training_letters_images_scaled.reshape([-1, 32, 32, 1])
testing_letters_images_scaled = testing_letters_images_scaled.reshape([-1, 32, 32, 1])
print(training_letters_images_scaled.shape, 
      training_letters_labels_encoded.shape, 
      testing_letters_images_scaled.shape, 
      testing_letters_labels_encoded.shape)
# (13440, 32, 32, 1) (13440, 28) (3360, 32, 32, 1) (3360, 28)


#----------------------------------------------------------------
#                         第六步 CNN模型设计
#----------------------------------------------------------------
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, BatchNormalization, Dropout, Dense

#定义模型
def create_model(optimizer='adam', kernel_initializer='he_normal', activation='relu'):
    #第一个卷积层
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=3, padding='same', input_shape=(32, 32, 1), kernel_initializer=kernel_initializer, activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(0.2))
    
    #第二个卷积层
    model.add(Conv2D(filters=32, kernel_size=3, padding='same', kernel_initializer=kernel_initializer, activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(0.2))
    
    #第三个卷积层
    model.add(Conv2D(filters=64, kernel_size=3, padding='same', kernel_initializer=kernel_initializer, activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(0.2))
    
    #第四个卷积层
    model.add(Conv2D(filters=128, kernel_size=3, padding='same', kernel_initializer=kernel_initializer, activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(0.2))
    model.add(GlobalAveragePooling2D())

    #全连接层输出28类结果
    model.add(Dense(28, activation='softmax'))

    #损失函数定义
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=optimizer)
    return model

#创建模型
model = create_model(optimizer='Adam', kernel_initializer='uniform', activation='relu')
model.summary()


#----------------------------------------------------------------
#                         第七步 模型绘制
#----------------------------------------------------------------
from keras.utils.vis_utils import plot_model
from IPython.display import Image as IPythonImage

plot_model(model, to_file="model.png", show_shapes=True)
display(IPythonImage('model.png'))


#----------------------------------------------------------------
#                         第八步 模型训练+输出结果
#----------------------------------------------------------------
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

#绘制图形
def plot_loss_accuracy(history):
    # Loss 
    plt.figure(figsize=[8,6])
    plt.plot(history.history['loss'],'r',linewidth=3.0)
    plt.plot(history.history['val_loss'],'b',linewidth=3.0)
    plt.legend(['Training loss', 'Validation Loss'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Loss',fontsize=16)
    plt.title('Loss Curves',fontsize=16)

    # Accuracy 
    plt.figure(figsize=[8,6])
    plt.plot(history.history['accuracy'],'r',linewidth=3.0)
    plt.plot(history.history['val_accuracy'],'b',linewidth=3.0)
    plt.legend(['Training Accuracy', 'Validation Accuracy'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Accuracy',fontsize=16)
    plt.title('Accuracy Curves',fontsize=16) 

#混淆矩阵
def get_predicted_classes(model, data, labels=None):
    image_predictions = model.predict(data)
    predicted_classes = np.argmax(image_predictions, axis=1)
    true_classes = np.argmax(labels, axis=1)
    return predicted_classes, true_classes, image_predictions

def get_classification_report(y_true, y_pred):
    print(classification_report(y_true, y_pred, digits=4)) #小数点4位

checkpointer = ModelCheckpoint(filepath='weights.hdf5', 
                               verbose=1, 
                               save_best_only=True)
flag = "test" 
if flag=="train":
    history = model.fit(training_letters_images_scaled, 
                        training_letters_labels_encoded,
                        validation_data=(testing_letters_images_scaled,
                                         testing_letters_labels_encoded),
                        epochs=15, 
                        batch_size=20, 
                        verbose=1, 
                        callbacks=[checkpointer])
    print(history)
    plot_loss_accuracy(history)
else:
    #加载具有最佳验证损失的模型
    model.load_weights('weights.hdf5')
    metrics = model.evaluate(testing_letters_images_scaled, 
                             testing_letters_labels_encoded, 
                             verbose=1)
    print("Test Accuracy: {}".format(metrics[1]))
    print("Test Loss: {}".format(metrics[0]))
    
    y_pred, y_true, image_predictions = get_predicted_classes(model, 
                                                              testing_letters_images_scaled, 
                                                              testing_letters_labels_encoded)
    get_classification_report(y_true, y_pred)


    #----------------------------------------------------------------
    #                         第九步 绘制测试图像
    #----------------------------------------------------------------
    fig = plt.figure(0, figsize=(14,14))
    indices = np.random.randint(0, testing_letters_labels.shape[0], size=49)
    y_pred = np.argmax(model.predict(training_letters_images_scaled), axis=1)

    for i, idx in enumerate(indices):
        plt.subplot(7,7,i+1)
            
        image_array = training_letters_images_scaled[idx][:,:,0]
        image_array = np.flip(image_array, 0)
        image_array = rotate(image_array, -90)
           
        plt.imshow(image_array, cmap='gray')
        plt.title("Pred: {} - Label: {}".format(y_pred[idx], 
                  (training_letters_labels[idx] -1)))
        plt.xticks([])
        plt.yticks([])
    plt.show()
    plt.savefig("resutl.png")



