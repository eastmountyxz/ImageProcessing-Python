# ImageProcessing-Python

---

该资源为作者在CSDN的撰写Python图像处理文章的支撑，主要是Python实现图像处理、图像识别、图像分类等算法代码实现。该系列文章是讲解Python OpenCV图像处理知识，前期主要讲解图像入门、OpenCV基础用法，中期讲解图像处理的各种算法，包括图像锐化算子、图像增强技术、图像分割等，后期结合深度学习研究图像识别、图像分类应用。希望该资源对您有所帮助，一起加油！

前文参考：

[[Python图像处理] 一.图像处理基础知识及OpenCV入门函数](https://blog.csdn.net/Eastmount/article/details/81748802) <br />
[[Python图像处理] 二.OpenCV+Numpy库读取与修改像素](https://blog.csdn.net/eastmount/article/details/82120114)  <br />
[[Python图像处理] 三.获取图像属性、兴趣ROI区域及通道处理](https://blog.csdn.net/eastmount/article/details/82177300) <br />
[[Python图像处理] 四.图像平滑之均值滤波、方框滤波、高斯滤波及中值滤波](https://blog.csdn.net/Eastmount/article/details/82216380)  <br />
[[Python图像处理] 五.图像融合、加法运算及图像类型转换](https://blog.csdn.net/Eastmount/article/details/82347501)  <br />
[[Python图像处理] 六.图像缩放、图像旋转、图像翻转与图像平移](https://blog.csdn.net/Eastmount/article/details/82454335)  <br />
[[Python图像处理] 七.图像阈值化处理及算法对比](https://blog.csdn.net/Eastmount/article/details/83548652)  <br />
[[Python图像处理] 八.图像腐蚀与图像膨胀](https://blog.csdn.net/Eastmount/article/details/83581277)  <br />
[[Python图像处理] 九.形态学之图像开运算、闭运算、梯度运算](https://blog.csdn.net/Eastmount/article/details/83651172)  <br />
[[Python图像处理] 十.形态学之图像顶帽运算和黑帽运算](https://blog.csdn.net/Eastmount/article/details/83692456)  <br />
[[Python图像处理] 十一.灰度直方图概念及OpenCV绘制直方图](https://blog.csdn.net/Eastmount/article/details/83758402)  <br />
[[Python图像处理] 十二.图像几何变换之图像仿射变换、图像透视变换和图像校正](https://blog.csdn.net/Eastmount/article/details/88679772)  <br />
[[Python图像处理] 十三.基于灰度三维图的图像顶帽运算和黑帽运算](https://blog.csdn.net/Eastmount/article/details/88712004)  <br />
[[Python图像处理] 十四.基于OpenCV和像素处理的图像灰度化处理](https://blog.csdn.net/Eastmount/article/details/88785768)  <br />
[[Python图像处理] 十五.图像的灰度线性变换](https://blog.csdn.net/Eastmount/article/details/88858696)  <br />
[[Python图像处理] 十六.图像的灰度非线性变换之对数变换、伽马变换](https://blog.csdn.net/Eastmount/article/details/88929290)  <br />
[[Python图像处理] 十七.图像锐化与边缘检测之Roberts算子、Prewitt算子、Sobel算子和Laplacian算子](https://blog.csdn.net/Eastmount/article/details/89001702)  <br />
[[Python图像处理] 十八.图像锐化与边缘检测之Scharr算子、Canny算子和LOG算子](https://blog.csdn.net/Eastmount/article/details/89056240)  <br />
[[Python图像处理] 十九.图像分割之基于K-Means聚类的区域分割](https://blog.csdn.net/Eastmount/article/details/89218513)  <br />
[[Python图像处理] 二十.图像量化处理和采样处理及局部马赛克特效](https://blog.csdn.net/Eastmount/article/details/89287543)  <br />
[[Python图像处理] 二十一.图像金字塔之图像向下取样和向上取样](https://blog.csdn.net/Eastmount/article/details/89341077)  <br />
[[Python图像处理] 二十二.Python图像傅里叶变换原理及实现](https://blog.csdn.net/Eastmount/article/details/89474405)  <br />
[[Python图像处理] 二十三.傅里叶变换之高通滤波和低通滤波](https://blog.csdn.net/Eastmount/article/details/89645301)  <br />
[[Python图像处理] 二十四.图像特效处理之毛玻璃、浮雕和油漆特效](https://blog.csdn.net/Eastmount/article/details/89853630)  <br />
[[Python图像处理] 二十五.图像特效处理之素描、怀旧、光照、流年以及滤镜特效](https://blog.csdn.net/Eastmount/article/details/99566969)  <br />


希望文章对您有所帮助，如果有不足之处，还请海涵~

原博客参考地址：[https://blog.csdn.net/eastmount/article/category/9278090](https://blog.csdn.net/eastmount/article/category/9278090)

CSDN Eastmount 杨秀璋
2019-10-17


---

效果图：


<div align=center><img src="https://img-blog.csdn.net/20180903142846357?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="60%" height="60%" />


<div align=center><img src="https://img-blog.csdn.net/20180830143424533?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="60%" height="60%" />



<div align=center><img src="https://img-blog.csdn.net/20180906130642638?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="60%" height="60%" />


<div align=center><img src="https://img-blog.csdnimg.cn/20181030211808848.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==,size_16,color_FFFFFF,t_70" width="60%" height="60%" />




  
 
