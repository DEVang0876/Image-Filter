# Object Tracking with OpenCV

## Overview

This project demonstrates **real-time object tracking** using OpenCV. The program uses the **CSRT (Channel and Spatial Reliability Tracking)** algorithm or other tracking algorithms from OpenCV's `cv2.Tracker` API to track objects in a video stream or a webcam feed. The user can select the object they want to track via a Region of Interest (ROI) selection box, and the program will automatically follow and highlight that object in real time.

This project aims to showcase the basics of object tracking in OpenCV using different tracking algorithms and how to implement them in a Python program.

## Features

- Real-time object tracking in a video stream or webcam feed.
- Ability to select the object to track via a Region of Interest (ROI) selection box.
- Draw bounding boxes around the tracked object.
- Option to exit or save the frames with tracked objects.

## Requirements

- **Python** 3.x
- **OpenCV** 4.x or later

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/DEVang0876/object-tracking.git
cd object-tracking
```

### Step 2: Set up the Python Environment

python3 -m venv object_tracking_env
source object_tracking_env/bin/activate  # On macOS/Linux


### Step 3: Install Dependencies

pip install opencv-python numpy


#### Usage:

Run .py file.
