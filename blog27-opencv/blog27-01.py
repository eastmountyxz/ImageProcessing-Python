# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 绘制图像函数
def display():
    # 清除屏幕及深度缓存
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # 设置红色
    glColor3f(1.0, 0.0, 0.0)
    # 开始绘制四边形
    glBegin(GL_QUADS)
    # 绘制四个顶点
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    # 结束绘制四边形
    glEnd()
    # 清空缓冲区并将指令送往硬件执行
    glFlush()

# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置大小
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("eastmount")
    # 调用display()函数绘制图像
    glutDisplayFunc(display)
    # 进入glut主循环
    glutMainLoop()
