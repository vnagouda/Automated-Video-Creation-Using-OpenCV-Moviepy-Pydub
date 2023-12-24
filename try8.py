# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 00:17:27 2023

@author: vnago
"""
import cv2
import numpy as np

# Set the video properties
width, height = 640, 480  # You can adjust the width and height as needed
fps = 30
duration = 20  # in seconds

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs like 'XVID' or 'MJPG'
out = cv2.VideoWriter('white_background_video.mp4', fourcc, fps, (width, height))

# Create frames with a white background
for _ in range(fps * duration):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background
    out.write(frame)
    
# Release the VideoWriter object
out.release()
