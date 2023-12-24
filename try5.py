import cv2
import numpy as np


def draw_box_top_center(frame, frame_number, keyframes,  box_width=600, box_height=200, padding_top=100):
    # Get the frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Calculate the position of the top center of the frame
    center_x = frame_width // 2
    top_y = padding_top
    
     # Calculate the position of the top center of the frame
    center_y = padding_top + box_height // 2
    # Calculate the x-coordinate of the box based on the frame number
    if frame_number < keyframes[0]:
        box_x = -box_width  # Start the box outside the left side of the frame
    elif frame_number >= keyframes[-1]:
        box_x = frame_width  # Move the box outside the right side of the frame
    else:
        # Interpolate the x-coordinate of the box between keyframes
        idx = np.searchsorted(keyframes, frame_number)
        t = (frame_number - keyframes[idx - 1]) / (keyframes[idx] - keyframes[idx - 1])
        box_x = int((1 - t) * 0 + t * frame_width)

    # Calculate the coordinates of the box
    box_top_left = (box_x, center_y - box_height // 2)
    box_bottom_right = (box_x + box_width, center_y + box_height // 2)

    # Create a copy of the frame to avoid modifying the original frame
    frame_with_box = frame.copy()

    # Draw the box on the frame
    cv2.rectangle(frame_with_box, box_top_left, box_bottom_right, (0, 255, 0), thickness=cv2.FILLED)

    return frame_with_box

def resize_video(video_path, output_path, target_resolution=(1080, 1920)):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the original video's frame width, height, and frames per second
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, target_resolution)

    # Calculate the crop dimensions to fit the target resolution while maintaining the aspect ratio
    target_width, target_height = target_resolution
    aspect_ratio = target_width / target_height
    if original_width / original_height > aspect_ratio:
        new_width = int(original_height * aspect_ratio)
        crop_x = int((original_width - new_width) / 2)
        crop_y = 0
    else:
        new_height = int(original_width / aspect_ratio)
        crop_x = 0
        crop_y = int((original_height - new_height) / 2)

    # Process each frame of the original video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Calculate new_height if it hasn't been calculated yet
        if 'new_height' not in locals():
            new_height = int(original_width / aspect_ratio)

        # Crop the frame to the target resolution
        cropped_frame = frame[crop_y:crop_y + new_height, crop_x:crop_x + new_width]

        # Resize the frame to the target resolution
        resized_frame = cv2.resize(cropped_frame, target_resolution)
        
        keyframes = [0,50,100,150,200]
        
        # Write the frame to the output video
        for frame_number in range(201):
            out.write(draw_box_top_center(resized_frame, frame_number, keyframes))

    # Release the video capture and writer objects
    cap.release()
    out.release()

if __name__ == "__main__":
    input_video_path = "PinPerfect1 (2).avi"
    output_video_path = "output_template.mp4"
    target_resolution = (1080, 1920)

    resize_video(input_video_path, output_video_path, target_resolution)
