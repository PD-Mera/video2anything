from moviepy.editor import VideoFileClip
import argparse
from utils import *

video_ext = ["avi", "mp4"]
gif_ext = ["gif"]


def video2gif(in_vid, out_vid, fps, height):
    assert fps is not None, "You must set fps in arguments"
    assert height is not None, "You must set height in arguments, 0 for not resize"

    if in_vid.split(".")[-1] not in video_ext:
        print(f"Input video file path error. Video file must end with {video_ext}")
        exit()
    if out_vid.split(".")[-1] not in gif_ext:
        print(f"Output gif file path error. Gif file must end with {video_ext}")
        exit()
    if fps is not None and fps <= 0:
        print(f"FPS must greater than 0")
        exit()

    videoClip = VideoFileClip(in_vid)

    if height != 0:
        videoClip = videoClip.resize(height=height)

    videoClip.write_gif(out_vid, fps=fps)

    print(f"Export gif file completed. Gif is saved in {out_vid}")
