#!/bin/bash
# Install dependencies
pip install -r requirements.txt --quiet
# Unzip example videos
mkdir -p video
unzip -n video.zip -d video
# Run and build the interface for inference
python app.py
