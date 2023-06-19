# Importing all necessary libraries
import cv2
import os
from ..utils.utils import *


def video2img(args):
    assert args.skip_frame is not None, "You must set skip_frame in arguments"

    # Read the video from specified path
    cam = cv2.VideoCapture(args.input)
    
    # creating a folder named data
    os.makedirs(args.output, exist_ok=True)
    
    # frame
    currentframe = 0
    count = -1
    
    while(True):
        
        # reading from frame
        ret,frame = cam.read()
        count += 1

        if count % args.skip_frame != 0:
            currentframe += 1
            continue
    
        if ret:
            # if video is still left continue creating images
            name = f'{args.output}/frame_' + str(currentframe) + '.jpg'
            print('Creating... ' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = basic_parser()
    parser.add_argument("--skip_frame", type=int, default=1)
    args = parser.parse_args()

    video2img(args)

