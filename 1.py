import os

import cv2
import numpy as np
import pandas as pd
def get_serval_frame(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_path, f'frame{i}.jpg')
        cv2.imwrite(frame_path, frame)
        frames.append(frame)
        i+=1

    cap.release()
    return frames

get_serval_frame(r'./video.mp4', r'./frame_get')
