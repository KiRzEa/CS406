# Training YOLO for Object Detection on GTSRB dataset
![](http://benchmark.ini.rub.de/Images/gtsrb/0.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/1.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/2.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/3.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/4.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/5.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/12.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/11.png)
![](http://benchmark.ini.rub.de/Images/gtsrb/8.png)

This repository contains scripts for training a YOLO model on GTSRB dataset for Object Detection task.
# Dataset #
[German Traffic Sign Recognition Dataset (GTSRB)](https://benchmark.ini.rub.de/gtsrb_news.html) is an image classification dataset.  
The images are photos of traffic signs. The images are classified into 43 classes. The training set contains 39209 labeled images and the test set contains 12630 images. Labels for the test set are not published.  
See more details [here](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset).
# Model #
YOLOv8 is the latest iteration in the YOLO series of real-time object detectors, offering cutting-edge performance in terms of accuracy and speed. Building upon the advancements of previous YOLO versions, YOLOv8 introduces new features and optimizations that make it an ideal choice for various object detection tasks in a wide range of applications.

# Libraries #
[Ultralytics](https://www.ultralytics.com/) with [PyTorch](http://pytorch.org/) backend.

# Metrics #
The model achieved 0.993 mAP50 and 0.943 mAP50-95 on test set (20% subset of original train set).
# Usage
## Train
To train the YOLO, run the notebook the folder Notebooks:
## Build interface using Gradio
```
bash run.sh
```
