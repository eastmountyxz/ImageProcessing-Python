# -*- coding: utf-8 -*-   
import os
from moviepy.editor import *

#递归获取文件名称
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.mp4':  
                L.append(os.path.join(root, file))  
    return L 

#主函数
if __name__ == '__main__':
    filePath = 'vedio'
    file_list = file_name(filePath)

    k = 1
    L = []
    for name in file_list:
        print(name)
        #获取视频总时间
        video = VideoFileClip(name)
        times = video.duration
        L.append(video)
        print(times)

    #视频合成 帧数大致就是24
    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile('./final.mp4', fps= 24, remove_temp=True)
        
