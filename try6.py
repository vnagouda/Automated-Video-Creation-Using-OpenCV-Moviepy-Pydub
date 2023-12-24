# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:07:04 2023

@author: vnago
"""

import cv2
import numpy as np

def animate_box(frame, box_position):
    # Define animation parameters
    box_width, box_height = 600, 200
    padding_top = 100

    # Calculate box position based on the given position
    box_x = int(box_position*100)  # Adjust the width as needed
    box_y = padding_top

    # Draw a solid box on the frame
    cv2.rectangle(frame, (box_x, box_y), (box_x + box_width, box_y + box_height), (0, 255, 0), thickness=cv2.FILLED)

    return frame

# Create a VideoCapture object
cap = cv2.VideoCapture("PinPerfect1 (2).avi")

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter("D:\Viresh\Assignment_Tutorials\YoutubeShortsGenerator\output_video_opencv.mp4", fourcc, fps, frame_size)

# Define keyframes for the animation
start_keyframe, stop_keyframe = 0, 5


# Process each frame and create the output video
for frame_number in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    if not ret:
        break

    # Get the corresponding keyframe position
    keyframe_position = min(frame_number / fps, keyframes[-1])

    # Apply the animation to the frame
    animated_frame = animate_box(frame.copy(), keyframe_position)

    # Write the frame to the output video
    output_video.write(animated_frame)

# Release resources
cap.release()
output_video.release()
cv2.destroyAllWindows()
