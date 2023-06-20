import cv2
import numpy as np


def resize(in_video, out_video, height, width):
    assert out_video.endswith(".avi"), "Output must end with .avi"
    cap = cv2.VideoCapture(in_video)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(out_video, fourcc, 5, (height, width))

    while True:
        ret, frame = cap.read()
        if ret is True:
            b = cv2.resize(
                frame, (height, width), fx=0, fy=0, interpolation=cv2.INTER_CUBIC
            )
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
