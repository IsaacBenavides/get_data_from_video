import moviepy.editor as mp
import sys

try:
    video = sys.argv[1]
    clip = mp.VideoFileClip(video)
    clip.audio.write_audiofile("audio.mp3")
except:
    print("Usage: \n - python get_audio.py [path for video]")
