# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:17:43 2023

@author: vnago
"""

import cv2
import numpy as np
from PIL import Image, ImageDraw
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import os
from pydub import AudioSegment

os.environ["FFMPEG_PATH"] = r"D:\Viresh\Assignment_Tutorials\YoutubeShortsGenerator\ffmpeg-6.1\ffmpeg-6.1" 
# Specify the path to the mediainfo executable
os.environ["MEDIAINFO_PATH"] = r"C:\Program Files\MediaInfo\MediaInfo.exe"  # Replace with the actual path to mediainfo executable



# Set the dimensions and frame rate of the video
width, height = 1080, 1920
fps = 30

# Create a VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_path = 'output_video_with_audio.avi'
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

background_video = VideoFileClip(r"D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/PinPerfect1 (2).avi")

# Create a loop to generate frames
for i in range(510):
    
     # Read a frame from the background video
    background_frame = background_video.get_frame(i/fps)
    background_frame = cv2.resize(background_frame, (width, height))
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    box_height = 150
    corner_radius = 20
    draw.rectangle([(400, 300), (800, 300+box_height)], fill="black")
    draw.pieslice([(0, 0), (corner_radius * 2, corner_radius * 2)], 180, 270, fill="black")
    draw.pieslice([(width - corner_radius * 2, 0), (width, corner_radius * 2)], 270, 360, fill="black")
    foreground_frame = np.array(img)

    # Add text to the foreground frame
    text = f'Frame {i + 1}'
    cv2.putText(foreground_frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Combine the foreground and background frames
    result_frame = cv2.addWeighted(background_frame, 0.1, foreground_frame, 0.9, 0)

    # Write the combined frame to the output video
    video_writer.write(result_frame)

# Release the video writer

#print(cv2.CAP_PROP_FRAME_COUNT)

audio_path = "Helium.mp3"
audio_clip = AudioSegment.from_file(audio_path, format="mp3")

# Get the duration of the video in seconds
video_duration = len(background_video) / background_video.fps

video_writer.release()
background_video.close()

# Trim or repeat the audio to match the video duration
adjusted_audio = audio_clip[:int(video_duration * 1000)]  # Convert seconds to milliseconds

# Export the adjusted audio to a new file
adjusted_audio_path = 'adjusted_audio.mp3'
adjusted_audio.export(adjusted_audio_path, format="mp3")

# Load the video again with audio
video_with_audio = VideoFileClip('D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/PinPerfect1 (2).avi')
video_with_audio = video_with_audio.set_audio(adjusted_audio)

# Write the final video with adjusted audio
final_output_path = 'final_output_with_adjusted_audio.mp4'
video_with_audio.write_videofile(final_output_path, codec='libx264', audio_codec='aac', fps=fps)

# Release resources
video_with_audio.close()
adjusted_audio.close()