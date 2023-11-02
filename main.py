import moviepy.editor

video = moviepy.editor.VideoFileClip('video_name.mp4')

audio = video.audio

audio.write_audiofile('audio_name.mp3')