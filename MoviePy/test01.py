from moviepy.editor import *

#视频旋转180度
clip = VideoFileClip("cat01.mp4").rotate(180)

#The size of the clip, (width,heigth) in pixels
print(clip.size) #(720, 1280)

#播放视频
#clip.ipython_display(width=100)

#写入视频
clip.write_videofile("cat01_rotate.mp4")
