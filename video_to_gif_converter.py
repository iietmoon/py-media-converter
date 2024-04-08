import os
from moviepy.editor import VideoFileClip

def convert_to_gif(video_path, output_folder):
    clip = VideoFileClip(video_path)
    gif_name = os.path.splitext(os.path.basename(video_path))[0] + ".gif"
    gif_output_path = os.path.join(output_folder, gif_name)
    clip.write_gif(gif_output_path, fps=10)
    clip.close()

def convert_videos_to_gif(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mov"):
            video_path = os.path.join(input_folder, file)
            convert_to_gif(video_path, output_folder)

if __name__ == "__main__":
    input_folder = "videos"
    output_folder = "output"
    convert_videos_to_gif(input_folder, output_folder)
