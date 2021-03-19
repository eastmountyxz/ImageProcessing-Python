# -*- coding:utf-8 -*-
# By:Eastmount CSDN 2021-03-19
import csv
import pandas as pd
import numpy as np
import jieba
import jieba.analyse

#添加自定义词典和停用词典
jieba.load_userdict("user_dict.txt")
stop_list = pd.read_csv('stop_words.txt',
                        engine='python',
                        encoding='utf-8',
                        delimiter="\n",
                        names=['t'])['t'].tolist()

#-----------------------------------------------------------------------
#Jieba分词函数
def txt_cut(juzi):
    return [w for w in jieba.lcut(juzi) if w not in stop_list]

#-----------------------------------------------------------------------
#中文分词读取文件
def fenci(filename,result):
    #写入分词结果
    fw = open(result, "w", newline = '',encoding = 'UTF-8')
    writer = csv.writer(fw)  
    writer.writerow(['label','cutword'])

    #使用csv.DictReader读取文件中的信息
    labels = []
    contents = []
    with open(filename, "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            #数据元素获取
            labels.append(row['label'])
            content = row['content']
            #中文分词
            seglist = txt_cut(content)
            #空格拼接
            output = ' '.join(list(seglist))
            contents.append(output)
            
            #文件写入
            tlist = []
            tlist.append(row['label'])
            tlist.append(output)
            writer.writerow(tlist)
    print(labels[:5])
    print(contents[:5])
    fw.close()

#-----------------------------------------------------------------------
#主函数
if __name__ == '__main__':
    fenci("news_dataset_train.csv", "news_dataset_train_fc.csv")
    fenci("news_dataset_test.csv", "news_dataset_test_fc.csv")
    fenci("news_dataset_val.csv", "news_dataset_val_fc.csv")
