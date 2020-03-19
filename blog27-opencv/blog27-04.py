# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

h = 0
m = 0
s = 0

# 绘制图像函数
def Draw():
    PI = 3.1415926
    R = 0.5
    TR = R - 0.05
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        glVertex2f(R * math.cos(2 * PI / 100 * i), R * math.sin(2 * PI / 100 * i))
    glEnd()
    glLineWidth(2)
    for i in range(100):
        glBegin(GL_LINES)
        glVertex2f(TR * math.sin(2 * PI / 12 * i), TR * math.cos(2 * PI / 12 * i))
        glVertex2f(R * math.sin(2 * PI / 12 * i), R * math.cos(2 * PI / 12 * i))
        glEnd()
    glLineWidth(1)

    h_Length = 0.2
    m_Length = 0.3
    s_Length = 0.4
    count = 60.0
    s_Angle = s / count
    count *= 60
    m_Angle = (m * 60 + s) / count
    count *= 12
    h_Angle = (h * 60 * 60 + m * 60 + s) / count
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(s_Length * math.sin(2 * PI * s_Angle), s_Length * math.cos(2 * PI * s_Angle))
    glEnd()
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(h_Length * math.sin(2 * PI * h_Angle), h_Length * math.cos(2 * PI * h_Angle))
    glEnd()
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(m_Length * math.sin(2 * PI * m_Angle), m_Length * math.cos(2 * PI * m_Angle))
    glEnd()
    glLineWidth(1)
    glBegin(GL_POLYGON)
    for i in range(100):
        glVertex2f(0.03 * math.cos(2 * PI / 100 * i), 0.03 * math.sin(2 * PI / 100 * i));
    glEnd()
    glFlush()

# 更新时间函数
def Update():
    global h, m, s
    t = time.localtime(time.time())
    h = int(time.strftime('%H', t))
    m = int(time.strftime('%M', t))
    s = int(time.strftime('%S', t))
    glutPostRedisplay()

# 主函数
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("My clock")
    glutDisplayFunc(Draw)
    glutIdleFunc(Update)
    glutMainLoop() 
