from utils import basic_parser
from convertor import video2gif, video2img


def full_parser():
    parser = basic_parser()

    ### video2img ###
    parser.add_argument("--video2img", action="store_true")
    parser.add_argument("--skip_frame", type=int, default=None)

    ### video2gif ###
    parser.add_argument("--video2gif", action="store_true")
    parser.add_argument("--fps", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    
    return parser



if __name__ == "__main__":
    parser = full_parser()
    args = parser.parse_args()

    if args.video2img:
        video2img(args)

    if args.video2gif:
        video2gif(args)

