from moviepy.editor import *
import random

#加载视频5-10片段
video = VideoFileClip("cat03.mp4").subclip(5,10)
times = video.duration

#在不同位置出现4次
n = 4  
times_list = [i * (times / n) for i in range(n + 1)]
#[0.0, 1.25, 2.5, 3.75, 5.0]
print(times_list) 
logos = []

#生成文本 自定义颜色字体
for i in range(n):
    txt_clip = TextClip("CSDN Eastmount 2020", fontsize=50, font='Simhei', color='blue')

    #显示时间 位置
    txt_clip = (txt_clip.set_start(times_list[i]).set_end(times_list[i + 1])
                .set_pos((random.randint(0, video.w), random.randint(0, video.h))))
    logos.append(txt_clip)

#Overlay text on video
result = CompositeVideoClip([video, *logos])

#写入文件 mp4文件默认用libx264编码 比特率单位bps
result.write_videofile("cat03_edited.mp4", codec="libx264", bitrate="10000000")
