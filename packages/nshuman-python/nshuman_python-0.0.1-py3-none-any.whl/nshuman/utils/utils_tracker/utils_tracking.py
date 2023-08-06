import os
import numpy as np
import cv2
#from tqdm import tqdm

from ..utils_pose.pose_util import draw_pose


def tracking_video(vid_path,save_path, detection_model, tracker,person=False,toRGB=True):
    cap = cv2.VideoCapture(vid_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)

    vid_writer = cv2.VideoWriter(
        save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (int(width), int(height))
    )

    while True:
        ret_val, frame = cap.read()
        if ret_val:
            track_plot = tracker.dttrack(detection_model,frame,toRGB=toRGB,person=person,return_type=1)
            track_plot = cv2.cvtColor(track_plot,cv2.COLOR_RGB2BGR)
            vid_writer.write(track_plot)
        else:
            break
    cap.release()
    vid_writer.release()

    print("Finish Tracking ...")
    print("Save:",save_path)
    return

def tracking_video_pose(vid_path,save_path, detection_model,pose_model, tracker,person=False,toRGB=True):
    cap = cv2.VideoCapture(vid_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)

    vid_writer = cv2.VideoWriter(
        save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (int(width), int(height))
    )

    while True:
        ret_val, frame = cap.read()
        if ret_val:
            online_tlwhs, online_ids, online_scores,track_plot = tracker.dttrack(detection_model,frame,toRGB=toRGB,person=person,return_type=3)
            results = pose_model.infer(frame,online_tlwhs,online_scores,toRGB=toRGB,box_format='xywh')
            track_plot = draw_pose(track_plot,results)
            track_plot = cv2.cvtColor(track_plot,cv2.COLOR_RGB2BGR)

            vid_writer.write(track_plot)
        else:
            break
    cap.release()
    vid_writer.release()

    print("Finish Tracking ...")
    print("Save:",save_path)
    return



