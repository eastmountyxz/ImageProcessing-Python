from moviepy.editor import *

#加载视频5-10片段
clip = VideoFileClip("cat02.mp4").subclip(5,10)
print(type(clip))

#降低音量x0.8
clip = clip.volumex(0.8)

#生成文本 自定义颜色字体
text = "CSDN Eastmount 2020"
txt_clip = TextClip(text, fontsize=70, font='Simhei', color='blue')

#屏幕中央显示5秒
txt_clip = txt_clip.set_position('center').set_duration(5)

#Overlay text on video
result = CompositeVideoClip([clip, txt_clip])

#写入文件
result.write_videofile("cat02_edited.mp4")
