#!/bin/bash
# Install dependencies
pip install -r requirements.txt --quiet
# Unzip example videos
unzip video.zip
# Run and build the interface for inference
python app.py
