#pip install moviepy
import moviepy.editor

#read video file
video = moviepy.editor.VideoFileClip('video_name.mp4')

#convert video to audio
audio = video.audio

#save the audio file
audio.write_audiofile('audio_name.mp3')
