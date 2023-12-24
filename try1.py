import os
import subprocess
from PIL import Image, ImageDraw

def create_frames(output_folder, output_video, num_frames=100, width=640, height=480):
    """
    Create frames and save them as images in the specified output folder.

    Parameters:
    - output_folder (str): The folder where frames will be saved.
    - num_frames (int): The number of frames to create.
    - width (int): Width of each frame.
    - height (int): Height of each frame.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_frames):
        # Create a new image
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)

        # Draw something on the image (example: a bouncing ball)
        ball_radius = 20
        x = (width - ball_radius) * (i / num_frames)
        y = height // 2 + int((height / 2) * abs((i - num_frames / 2) / (num_frames / 2)))

        draw.ellipse((x - ball_radius, y - ball_radius, x + ball_radius, y + ball_radius), fill="blue")

        # Save the image
        img.save(os.path.join(output_folder, f"{i + 1:04d}.png"))
        
        create_video(output_folder, output_video)
    

def create_video(input_folder, output_video, framerate=30, codec='libx264', crf=20, pix_fmt='yuv420p'):
    """
    Create a video from a sequence of image frames using ffmpeg.

    Parameters:
    - input_folder (str): Path to the folder containing image frames.
    - output_video (str): Path to the output video file.
    - framerate (int): Frames per second (default is 30).
    - codec (str): Video codec to use (default is 'libx264').
    - crf (int): Constant rate factor for video compression (default is 20).
    - pix_fmt (str): Pixel format for the video (default is 'yuv420p').
    """
    cmd = (
        f"ffmpeg -framerate {framerate} -i {input_folder}/%04d.png "
        f"-c:v {codec} -profile:v high -crf {crf} -pix_fmt {pix_fmt} {output_video}"
    )
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    output_folder = "D:/Viresh/Assignment_Tutorials/YoutubeShortsGenerator/frames"
    output_video = "output.mp4"

    # Create frames
    create_frames(output_folder, output_video)

    # Create video
    #create_video(output_folder, output_video)

    # Clean up frames (optional)
    # os.system(f"rm -r {output_folder}")