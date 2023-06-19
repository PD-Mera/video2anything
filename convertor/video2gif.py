from moviepy.editor import VideoFileClip
import argparse
from utils import *

video_ext = ['avi', 'mp4']
gif_ext = ['gif']

def video2gif(args):
    if args.input.split(".")[-1] not in video_ext:
        print(f"Input video file path error. Video file must end with {video_ext}")
        exit()
    if args.output.split(".")[-1] not in gif_ext:
        print(f"Output gif file path error. Gif file must end with {video_ext}")
        exit()
    if args.fps is not None and args.fps <= 0:
        print(f"FPS must greater than 0")
        exit()

    videoClip = VideoFileClip(args.input)

    if args.height is not None:
        videoClip = videoClip.resize(height=args.height)

    videoClip.write_gif(args.output, fps=args.fps)

    print(f"Export gif file completed. Gif is saved in {args.output}")


if __name__ == "__main__":
    parser = basic_parser()
    parser.add_argument("--fps", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    args = parser.parse_args()

    video2gif(args)

