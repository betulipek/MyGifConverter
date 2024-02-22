from moviepy.editor import  *

clip_mp4 = VideoFileClip("Madonna.mp4")
clip_mp4 = clip_mp4.subclip(5, 10)

clip_gif = clip_mp4.write_gif("Madonna.gif")


