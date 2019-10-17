#encoding:utf-8
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#绘制sin函数曲线
x1 = np.arange(0, 6, 0.1)
y1 = np.sin(x1)
plt.plot(x1, y1)

#绘制坐标点折现
x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [0.3, 0.4, 2.5, 3.4, 4, 5.8, 7.2]
plt.plot(x2, y2)

#省略有规则递增的x2参数 
y3 = [0, 0.5, 1.5, 2.4, 4.6, 8]
plt.plot(y3, color="r")

plt.show()
