# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

#生成随机数表示点的坐标
x = np.random.randn(200)
y = np.random.randn(200)

#生成随机点的大小及颜色
size = 50*np.random.randn(200) 
colors = np.random.rand(200)

#用来正常显示中文标签
plt.rc('font', family='SimHei', size=13)

#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False  

#绘制散点图
plt.scatter(x, y, s=size, c=colors)

#设置x、y轴名称
plt.xlabel(u"x坐标")  
plt.ylabel(u"y坐标")

#绘制标题
plt.title(u"Matplotlib绘制散点图")

#显示图像
plt.show()
