# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 绘制图像函数
def display():
    # 清除屏幕及深度缓存
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # 绘制线段
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)       # 左下角顶点
    glVertex2f(1.0, 0.0)        # 右下角顶点
    glVertex2f(0.0, 1.0)        # 右上角顶点
    glVertex2f(0.0, -1.0)       # 左上角顶点
    glEnd()

    # 绘制顶点
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)    # 红色
    glVertex2f(0.3, 0.3)
    glColor3f(0.0, 1.0, 0.0)    # 绿色
    glVertex2f(0.5, 0.6)
    glColor3f(0.0, 0.0, 1.0)    # 蓝色
    glVertex2f(0.9, 0.9)
    glEnd()

    # 绘制四边形
    glColor3f(1.0, 1.0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, 0.2)
    glEnd()

    # 绘制多边形
    glColor3f(0.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.1)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.5, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.2, -0.3)
    glEnd()

    # 绘制三角形
    glColor3f(1.0, 1.0, 1.0)
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.2, -0.6)
    
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
    # 设置窗口位置及大小
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(500, 300)
    # 创建窗口
    glutCreateWindow("CSDN Eastmount")
    # 调用display()函数绘制图像
    glutDisplayFunc(display)
    # 进入glut主循环
    glutMainLoop()
