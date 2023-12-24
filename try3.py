import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip

# Set video dimensions
width, height = 1080, 1920
frame_dimensions = (width, height)

# Set video duration and frames per second (fps)
duration_seconds = 18
fps = 30

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('output_video.mp4', fourcc, fps, frame_dimensions)

# Create black background
white_background = 255*np.ones((height, width, 3), dtype=np.uint8)

# Set dimensions for the white solid box
initial_box_width, initial_box_height = 640, 480
box_width, box_height = initial_box_width, initial_box_height
box_position = ((width - box_width) // 2, (height - box_height) // 2)
box_color = (0, 0, 0)  # White color

# Set initial dimensions for the first white solid box
initial_box1_width, initial_box1_height = 640, 480
box1_width, box1_height = initial_box1_width, initial_box1_height
box1_color = (0, 0, 0)  # Black color

# Animation keyframes for the first box
keyframes_box1 = [
    {"time": 0, "width": initial_box1_width, "height": initial_box1_height, "color": (0, 0, 0)},
    {"time": 5, "width": 320, "height": 240, "color": (255, 0, 0)},
    {"time": 10, "width": initial_box1_width, "height": initial_box1_height, "color": (0, 0, 255)}
]

# Set initial dimensions for the second white solid box
initial_box2_width, initial_box2_height = 480, 360
box2_width, box2_height = initial_box2_width, initial_box2_height
box2_color = (0, 255, 0)  # Green color

# Animation keyframes for the second box
keyframes_box2 = [
    {"time": 5, "width": initial_box2_width, "height": initial_box2_height, "color": (0, 255, 0)},
    {"time": 10, "width": 240, "height": 180, "color": (0, 0, 255)}
]

# Generate video frames
for frame_number in range(int(duration_seconds * fps)):
    
    # Generate video frames
    frame = white_background.copy()

    # Determine which set of keyframes to use based on time
    if frame_number / fps < 5:
        keyframes = keyframes_box1
    else:
        keyframes = keyframes_box2
        
    # Find the appropriate keyframes for the current time
    for i in range(len(keyframes) - 1):
        if keyframes[i]["time"] <= frame_number / fps < keyframes[i + 1]["time"]:
            t = (frame_number / fps - keyframes[i]["time"]) / (keyframes[i + 1]["time"] - keyframes[i]["time"])
            if keyframes == keyframes_box1:
                box1_width = int((1 - t) * keyframes[i]["width"] + t * keyframes[i + 1]["width"])
                box1_height = int((1 - t) * keyframes[i]["height"] + t * keyframes[i + 1]["height"])
                box1_color = (
                    int((1 - t) * keyframes[i]["color"][0] + t * keyframes[i + 1]["color"][0]),
                    int((1 - t) * keyframes[i]["color"][1] + t * keyframes[i + 1]["color"][1]),
                    int((1 - t) * keyframes[i]["color"][2] + t * keyframes[i + 1]["color"][2])
                )
            else:
                box2_width = int((1 - t) * keyframes[i]["width"] + t * keyframes[i + 1]["width"])
                box2_height = int((1 - t) * keyframes[i]["height"] + t * keyframes[i + 1]["height"])
                box2_color = (
                    int((1 - t) * keyframes[i]["color"][0] + t * keyframes[i + 1]["color"][0]),
                    int((1 - t) * keyframes[i]["color"][1] + t * keyframes[i + 1]["color"][1]),
                    int((1 - t) * keyframes[i]["color"][2] + t * keyframes[i + 1]["color"][2])
                )
            break
        
    padding_top = 50
    float_amplitude = 50
    float_frequency = 1.5
    float_offset = int(float_amplitude * np.sin(2 * np.pi * float_frequency * frame_number / fps))
    box_position = ((width - box_width) // 2, padding_top + float_offset)

    
    # Draw white solid box
    cv2.rectangle(frame, box_position, (box_position[0] + box_width, box_position[1] + box_height), box_color, -1)
    
    box_center = ((box_position[0] + box_position[0] + box_width) // 2, (box_position[1] + box_position[1] + box_height) // 2)
    
     # Add text at the center of the box
    if frame_number / fps < 5:
        text = f"Frame: {frame_number}"
    else:
        text = f"Frame: {frame_number - int(5 * fps)}"
    # Add text at the center of the box
    text = f"Frame: {frame_number}"
    text_position = (box_center[0] - 50, box_center[1] + 10)  # Adjust the text position as needed

    text_color = (255, 255, 255)  # White text color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    cv2.putText(frame, text, text_position, font, font_scale, text_color, 2, cv2.LINE_AA)
    
     # Add centered animation to the second box (adjust parameters as needed)
     # Add floating animation to the first box (adjust parameters as needed)
    padding_top_box1 = 50
    float_amplitude_box1 = 50
    float_frequency_box1 = 1.5
    float_offset_box1 = int(float_amplitude_box1 * np.sin(2 * np.pi * float_frequency_box1 * frame_number / fps))
    box1_position = ((width - box1_width) // 2, padding_top_box1 + float_offset_box1)

    box2_position = ((width - box2_width) // 2, height - 50 - box2_height)

    # Draw animated solid boxes
    cv2.rectangle(frame, box1_position, (box1_position[0] + box1_width, box1_position[1] + box1_height), box1_color, -1)
    cv2.rectangle(frame, box2_position, (box2_position[0] + box2_width, box2_position[1] + box2_height), box2_color, -1)

    # Add text at the center of the first box
    text_box1 = f"Frame: {frame_number}"
    text_position_box1 = (box1_position[0] + 20, box1_position[1] + 40)  # Adjust the text position as needed
    text_color = (255, 255, 255)  # White text color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    cv2.putText(frame, text_box1, text_position_box1, font, font_scale, text_color, 2, cv2.LINE_AA)


    # Write frame to video
    video_writer.write(frame)

    # Write frame to video
    video_writer.write(frame)

# Release VideoWriter object
video_writer.release()

# Load the video clip
video_clip = VideoFileClip('output_video.mp4')

# Load the audio clip (replace 'your_audio.mp3' with the path to your audio file)
audio_clip = AudioFileClip('Helium.mp3').subclip(0, duration_seconds*2)

# Add the audio to the video
video_clip = video_clip.set_audio(audio_clip)

# Write the final video with audio
video_clip.write_videofile('output_video_with_audio.mp4', codec='libx264', audio_codec='aac', fps=fps)

print("Video creation with audio completed.")
