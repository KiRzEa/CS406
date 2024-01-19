import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np
import os

# Load your YOLOv5 model from Ultralytics
model = YOLO('best.pt')

def save_video(frames, output_video_path, fps=30):
    # Get the height and width from the first frame
    height, width, _ = frames[0].shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each frame to the video file
    for frame in frames:
        out.write(frame)

    # Release the VideoWriter
    out.release()

def predict_video(input_video_path):
    output = "result.mp4"
    # Open the video file
    results = model.predict(input_video_path, vid_stride=True)

    frames = [im.plot() for im in results]
    
    save_video(frames, 'result.mp4')
    return output

# Define Gradio interface for video
iface = gr.Interface(
    fn=predict_video,
    inputs=gr.Video(),
    outputs="playable_video",
    examples=[
        'video/video1.mp4',
        'video/video2.mp4',
        'video/video3.mp4',
        'video/video4.mp4',
        'video/video5.mp4',
    ],
    cache_examples=True
)

# Launch the Gradio interface for video
iface.launch()