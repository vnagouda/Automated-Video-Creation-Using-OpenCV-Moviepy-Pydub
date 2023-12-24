# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:30:08 2023

@author: vnago
"""
from moviepy.editor import VideoFileClip, AudioFileClip

import os


# Specify the path to your video folder
folder_path = 'D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/OutputVideos'

# Use os.listdir() to get a list of all files in the directory
# Alternatively, you can use glob.glob() to filter files based on their extension
# For example, to get all .mp4 files: video_files = glob.glob(os.path.join(folder_path, '*.mp4'))
video_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mkv'))]

# Iterate through each video file
count = 0 
for video_file in video_files:
    # Construct the full path to the video file
    full_path = os.path.join(folder_path, video_file)
    existing_video = VideoFileClip(full_path)
    
    # Load audio file
    if count%2 == 0:
        additional_audio = AudioFileClip("Spacetime Blues - Loopop.mp3")
        # Ensure that the additional audio matches the duration of the video
        additional_audio = additional_audio.set_duration(existing_video.duration)
        # Set the audio of the existing video to the additional audio
        video_with_audio = existing_video.set_audio(additional_audio)
    elif count%3 == 0:
        additional_audio = AudioFileClip("D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/Time Passing By - Audionautix.mp3")
        # Ensure that the additional audio matches the duration of the video
        additional_audio = additional_audio.set_duration(existing_video.duration)
        # Set the audio of the existing video to the additional audio
        video_with_audio = existing_video.set_audio(additional_audio)
    elif count%5 == 0:
        additional_audio = AudioFileClip("Lands Unknown - Futuremono.mp3")
        # Ensure that the additional audio matches the duration of the video
        additional_audio = additional_audio.set_duration(existing_video.duration)
        # Set the audio of the existing video to the additional audio
        video_with_audio = existing_video.set_audio(additional_audio)
    elif count%1 == 0:
        additional_audio = AudioFileClip("Landing - Public Memory.mp3")
        # Ensure that the additional audio matches the duration of the video
        additional_audio = additional_audio.set_duration(existing_video.duration)
        # Set the audio of the existing video to the additional audio
        video_with_audio = existing_video.set_audio(additional_audio)
    else:
        additional_audio = AudioFileClip("Landing - Public Memory.mp3")
        # Ensure that the additional audio matches the duration of the video
        additional_audio = additional_audio.set_duration(existing_video.duration)
        # Set the audio of the existing video to the additional audio
        video_with_audio = existing_video.set_audio(additional_audio)
        
    # Write the result to a new file
    output_file = f"D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/OutputVideosWithAudio/Riddles{count}.mp4"
    video_with_audio.write_videofile(output_file, codec="libx264", audio_codec="aac")
    
    count += 1
    # Close the video clips
    existing_video.close()
    additional_audio.close()
    # Your code to process each video file goes here
    # For example, you might want to use a video processing library like OpenCV
    # to perform operations on each video file
    print("Processing:", full_path)