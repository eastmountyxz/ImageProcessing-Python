# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:26:27 2021
@author: xiuzhang
"""

from imageai.Detection import ObjectDetection

#实例化
detector = ObjectDetection()

#路径定义
model_path = "./models/yolo-tiny.h5"
input_path = "./input/person-02.png"
output_path = "./output/person-02.png"

#预训练模式
detector.setModelTypeAsTinyYOLOv3()

#设置预训练模型路径
detector.setModelPath(model_path)

#加载模型
detector.loadModel()

#创建对象
detection = detector.detectObjectsFromImage(input_image=input_path, 
                                            output_image_path=output_path)

#检测结果
for eachItem in detection:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
    
    
