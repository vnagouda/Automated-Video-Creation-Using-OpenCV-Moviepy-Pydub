# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:58:27 2023

@author: vnago
"""

import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip

# Set video dimensions
width, height = 1080, 1920
frame_dimensions = (width, height)

# Set video duration and frames per second (fps)
duration_seconds = 20
fps = 30

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('newOutput_video.mp4', fourcc, fps, frame_dimensions)

# Create black background
white_background = 255*np.ones((height, width, 3), dtype=np.uint8)
# Set dimensions for the white solid box
initial_box_width, initial_box_height = 640, 480
box_width, box_height = initial_box_width, initial_box_height
box_position = 200, 400
box_color = (0, 0, 0)  # black color

# Animation keyframes for the first box
keyframes_box1 = [
    {"time": 0, "width": initial_box_width, "height": initial_box_height, "color": (0, 0, 0), "position": (100,200)},
    {"time": 5, "width": initial_box_width, "height": initial_box_height, "color": (255, 0, 0), "position": (100, 600)},
]

for frame_number in range(int(duration_seconds * fps)):
    
    # Generate video frames
    frame = white_background.copy()
    initial_box_width, initial_box_height = 800, 300
    box_width, box_height = initial_box_width, initial_box_height
    keyframes = keyframes_box1
    
    box_color = (0, 0, 0) 
    
    for i in range(len(keyframes) - 1):
        if keyframes[i]["time"] <= frame_number / fps < keyframes[i + 1]["time"]:
            t = (frame_number / fps - keyframes[i]["time"]) / (keyframes[i + 1]["time"] - keyframes[i]["time"])
        
            box1_width = int((1 - t) * keyframes[i]["width"] + t * keyframes[i + 1]["width"])
            box1_height = int((1 - t) * keyframes[i]["height"] + t * keyframes[i + 1]["height"])
            box1_color = (
                int((1 - t) * keyframes[i]["color"][0] + t * keyframes[i + 1]["color"][0]),
                int((1 - t) * keyframes[i]["color"][1] + t * keyframes[i + 1]["color"][1]),
                int((1 - t) * keyframes[i]["color"][2] + t * keyframes[i + 1]["color"][2])
            )
        
    # Draw white solid box
    cv2.rectangle(frame, box_position, (box_position[0] + box_width, box_position[1] + box_height), box_color, -1)
    
    box_center = ((box_position[0] + box_position[0] + box_width) // 2, (box_position[1] + box_position[1] + box_height) // 2)
    text = f"Frame: {frame_number}"
    text_position = (box_center[0] - 50, box_center[1] + 10)  # Adjust the text position as needed

    text_color = (255, 255, 255)  # White text color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    cv2.putText(frame, text, text_position, font, font_scale, text_color, 2, cv2.LINE_AA)
    # Write frame to video
    video_writer.write(frame)

    # Write frame to video
    video_writer.write(frame)


video_writer.release()

