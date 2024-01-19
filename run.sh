#!/bin/bash
# Install dependencies
pip install -r requirements.txt --quiet
# Unzip weight file
unzip -n weights/best.zip -d weights
# Unzip example videos
mkdir -p video
unzip -n video.zip -d video
# Run and build the interface for inference
python app.py
