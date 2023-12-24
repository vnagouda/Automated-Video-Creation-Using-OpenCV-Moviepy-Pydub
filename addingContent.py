# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:27:35 2023

@author: vnago
"""

import pandas as pd
import cv2
import numpy as np
import try7
from moviepy.editor import VideoFileClip
# Specify the path to your Excel file
excel_file_path = 'Book1.xlsx'

# Load the Excel sheet into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Now, you can work with the data in the DataFrame
# For example, you can print the first few rows of the DataFrame
print(df.dtypes)

# Set video properties
width, height = 1080, 1920
fps = 30
duration = 20  # in seconds


# Create a white background image
video_background = VideoFileClip("BackgroundVideo1.mp4", audio=(True))
video_background = video_background.resize((width, height))

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
    
# Write frames to the video
for index, row in df.iterrows():
    
    title = str(row['Title'])
    question = str(row['Body'])
    opt1 = str(row['Option 1'])
    opt2 = str(row['Option 2'])
    opt3 = str(row['Option 3'])
    ans = str(row['Answer'])
    output_file = f'{title}{index}.mp4'
    #count = 0
    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    
    background_frame_count = int(fps*duration)*(index)
    #output_file = f'output_video{index}.mp4'
    for frame_number in range(int(fps * duration)):
        # Add your content to each frame if needed
        boxTime = frame_number//fps
        # For example, draw a rectangle in the center
        tempBox_x = boxEmoji_x
        tempHook_x = (center_x//2)+100 
        tempBox_x = tempBox_x + (frame_number//2)+ 100
        tempHook_x = tempHook_x + (frame_number//2) + 100
        
        if boxTime >= 3 and boxTime <= 13:
            #white_background = np.ones((height, width, 3), dtype=np.uint8) * 255
            current_frame = video_background.get_frame((frame_number+background_frame_count)/ fps)
            white_background = (current_frame * 255).astype(np.uint8)
            #Question
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 6 -400),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 6 -200), (0, 255, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y - 450, rectangle_size, rectangle_size//3+200), question)
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 8 + 100),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 8 + 100), (0, 255, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y + 50, rectangle_size, rectangle_size//4), opt1, font_scale=2)
            # opt2
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 8 + 300),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 8 + 300), (0, 255, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y + 250, rectangle_size, rectangle_size//4), opt2, font_scale=2)
            #opt3
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 8 + 500),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 8 + 500), (0, 255, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y + 450, rectangle_size, rectangle_size//4), opt3, font_scale=2)
            #Timer
            cv2.rectangle(white_background, (boxEmoji_x - boxEmojiWidth // 2, boxEmoji_y - boxEmojiHeight // 4 + 100),
              (boxEmoji_x + boxEmojiWidth // 2, boxEmoji_y + boxEmojiHeight // 4 + 100), (0, 0, 255), cv2.FILLED)
            white_background = try7.put_text_in_hook_box(white_background, (boxEmoji_x - boxEmojiWidth // 2, boxEmoji_y - boxEmojiHeight // 4 + 100, boxEmojiWidth, boxEmojiHeight), f"{13 - frame_number//fps}")
        elif boxTime > 13:
            current_frame = video_background.get_frame((frame_number+background_frame_count) / fps)
            white_background = (current_frame * 255).astype(np.uint8)
            #Question
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 6 -400),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 6 -200), (255, 0, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y - 450, rectangle_size, rectangle_size//3+200), question)
            # Ans
            cv2.rectangle(white_background, (center_x - rectangle_size // 2, center_y - rectangle_size // 8 + 300),
                  (center_x + rectangle_size // 2, center_y + rectangle_size // 8 + 300), (255, 0, 0), cv2.FILLED)
            white_background = try7.put_text_in_question_box(white_background, (center_x - rectangle_size // 2 , center_y + 250, rectangle_size, rectangle_size//4), ans, font_scale=2)
            #gif
            cv2.rectangle(white_background, (tempBox_x - boxEmojiWidth // 2, boxEmoji_y - boxEmojiHeight // 2),
                  (tempBox_x + boxEmojiWidth // 2, boxEmoji_y + boxEmojiHeight // 2), (0, 0, 255), cv2.FILLED)   
            
        else:
            current_frame = video_background.get_frame((frame_number+background_frame_count) / fps)
            white_background = (current_frame * 255).astype(np.uint8)
            #gif
            cv2.rectangle(white_background, (tempBox_x - boxEmojiWidth // 2, boxEmoji_y - boxEmojiHeight // 2),
                  (tempBox_x + boxEmojiWidth // 2, boxEmoji_y + boxEmojiHeight // 2), (0, 0, 255), cv2.FILLED)
            white_background[boxEmoji_y - boxEmojiHeight // 2:boxEmoji_y + boxEmojiHeight // 2,
                             tempBox_x - boxEmojiWidth // 2:tempBox_x + boxEmojiWidth // 2] = emoji
            #Hook
            cv2.rectangle(white_background, (tempHook_x - rectangle_size // 2, center_y - rectangle_size // 2),
                  (tempHook_x + rectangle_size // 2, center_y + rectangle_size // 2), (0, 0, 255), cv2.FILLED)
            white_background = try7.put_text_in_hook_box(white_background, (tempHook_x - rectangle_size // 2, center_y - rectangle_size // 2, rectangle_size, rectangle_size), "Are you smarter than a 5th grader?")
            
        # Write the frame to the video
        tempTitle_x = boxTitle_x + 100 
        tempTitle_x = tempTitle_x + (frame_number*2)
        if boxTime <= duration:
            if tempTitle_x <= width//2:
                #Title
                cv2.rectangle(white_background, (tempTitle_x - boxTitleWidth // 2, boxTitle_y - boxTitleHeight // 2),
                      (tempTitle_x + boxTitleWidth // 2, boxTitle_y + boxTitleHeight // 2), (0, 0, 255), cv2.FILLED)
                white_background = try7.put_text_in_title_box(white_background, (tempTitle_x + 100 - boxTitleWidth // 2, boxTitle_y - boxTitleHeight // 2, boxTitleWidth, boxTitleHeight), title)
            else:
                #Title
                cv2.rectangle(white_background, ((boxTitle_x*2) - boxTitleWidth // 2, boxTitle_y - boxTitleHeight // 2),
                      ((boxTitle_x*2) + boxTitleWidth // 2, boxTitle_y + boxTitleHeight // 2), (0, 0, 255), cv2.FILLED)
                white_background = try7.put_text_in_title_box(white_background, ((boxTitle_x*2) + 100 - boxTitleWidth // 2, boxTitle_y - boxTitleHeight // 2, boxTitleWidth, boxTitleHeight), title)
        else:
            current_frame = video_background.get_frame((frame_number+background_frame_count) / fps)
            white_background = (current_frame * 255).astype(np.uint8)
        
        out.write(white_background)
    
    
    out.release()
    print(f"Video saved as {output_file}")
    
    
    
   
