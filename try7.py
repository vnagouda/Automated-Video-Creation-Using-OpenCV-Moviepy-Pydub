# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:37:22 2023

@author: vnago
"""



import cv2
import numpy as np

# Set video properties
width, height = 1080, 1920
fps = 30
duration = 20  # in seconds
output_file = 'output_video.mp4'

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Create a white background image
white_background = np.ones((height, width, 3), dtype=np.uint8) * 255

#making the different boxes i need
#1 Title
boxTitle_x, boxTitle_y = width // 4 ,200
boxTitleWidth, boxTitleHeight = 600,200

#2 Hook
center_x, center_y = width // 2, height // 2
rectangle_size = 700

#3 Emoji
boxEmoji_x, boxEmoji_y = width // 4, 1600
boxEmojiWidth, boxEmojiHeight = 300,300

emoji_path = 'D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/pngwing.com.png'
emoji = cv2.imread(emoji_path)
if emoji is None:
    print(f"Error: Unable to load the emoji image at {emoji_path}")
    # Handle the error or choose another emoji path
else:
    emoji = cv2.resize(emoji, (boxEmojiWidth, boxEmojiHeight))
    
    
#emoji = cv2.resize(emoji, (boxEmojiWidth, boxEmojiHeight))

# Function to put text in the center of a box
def put_text_in_title_box(image, box_coordinates, text, font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, font_scale=2, font_thickness=2, text_color=(0, 0, 0)):
    # Create a copy of the image to avoid modifying the original
    result_image = image.copy()

    # Extract box coordinates
    x, y, width, height = box_coordinates
    
    # Get the size of the text
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    #print(text_size)
    # Calculate the position to center the text in the box
    text_x = x - (width - text_size[0])//2
    text_y = y + (height + text_size[1])//2
    
    # Put the text in the center of the box
    cv2.putText(result_image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

    return result_image

def put_text_in_question_box(image, box_coordinates, text, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=2, font_thickness=2, text_color=(0, 0, 0)):
    result_image = image.copy()

    x, y, width, height = box_coordinates

    # Split the text into lines based on width
    lines = []
    current_line = ""
    for word in text.split():
        # Check the width of the current line with the new word
        text_size, _ = cv2.getTextSize(current_line + word, font, font_scale, font_thickness)

        # If the line becomes too wide, start a new line
        if text_size[0] > width:
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line += word + " "

    # Add the last line
    lines.append(current_line.strip())

    # Calculate the total height of all lines
    total_text_height = len(lines) * (text_size[1] + 2)

    # Calculate the starting y-position to center the text in the box vertically
    text_y = y + (height - total_text_height) // 2

    # Draw the box
    #cv2.rectangle(result_image, (x, y), (x + width, y + height), (255, 0, 0), 2)

    # Put the text in the box, handling line breaks
    for line in lines:
        text_size, baseline = cv2.getTextSize(line, font, font_scale, font_thickness)
        text_x = x + (width - text_size[0]) // 2
        cv2.putText(result_image, line, (text_x, text_y), font, font_scale, text_color, font_thickness)
        text_y += text_size[1] + 2  # Add a small vertical space between lines

    return result_image

def put_text_in_hook_box(image, box_coordinates, text, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=4.5, font_thickness=2, text_color=(0, 0, 0)):
    result_image = image.copy()

    x, y, width, height = box_coordinates

    # Split the text into lines based on width
    lines = []
    current_line = ""
    for word in text.split():
        # Check the width of the current line with the new word
        text_size, _ = cv2.getTextSize(current_line + word, font, font_scale, font_thickness)

        # If the line becomes too wide, start a new line
        if text_size[0] > width:
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line += word + " "

    # Add the last line
    lines.append(current_line.strip())

    # Calculate the total height of all lines
    total_text_height = len(lines) * (text_size[1] + 2)

    # Calculate the starting y-position to center the text in the box vertically
    text_y = y + (height - total_text_height) // 2

    # Draw the box
    #cv2.rectangle(result_image, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Put the text in the box, handling line breaks
    for line in lines:
        text_size, baseline = cv2.getTextSize(line, font, font_scale, font_thickness)
        text_x = x + (width - text_size[0]) // 2
        cv2.putText(result_image, line, (text_x, text_y), font, font_scale, text_color, font_thickness)
        text_y += text_size[1] + 2  # Add a small vertical space between lines

    return result_image