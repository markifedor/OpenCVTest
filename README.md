# OpenCV Test Project

## Overview

This is a learning test for OpenCV with image processing functions using the camera that includes edge detection, corner detection, blurring, color space conversion, and flipping in the ``CV_1-Visual-Effects-Test.py`` file, and exposure, contrast, and color space conversion in the ``CV_2-Visual-Effects-ExpHue-Test.py`` file. 

Exit of the window is with the ``q`` key or ``Esc``. 

Running either file will open a new window and access your first index camera

Different modes change the video feed:

In the first file:

* Pressing "N" turns the footage back to normal
* Pressing "E" turns on edge detection
* Pressing "B" blurs the feed
* Pressing "C" turns on corner detection
* Pressing "F" goes through all flipped orientations
* Pressing "M" goes through some color modes (Default, Inverse, BGR2HSV, and Grayscale)

In the second file:

* Pressing "N" turns the footage back to normal
* Pressing "M" goes through some color modes (Default, Inverse, BGR2HSV, and Grayscale)
* Pressing "B" brightens the original footage
* Pressing "D" darkens the original footage
* Pressing "H" turns up the contrast of the original footage
* Pressing "L" turns down the contrast of the original footage

\*Note that only the color mode and flip can be combined with the other filter\*

## Installation Process
### Install Pip Environment
make folder:

    mkdir <folder>

Go to folder:

    cd <folder>

Make virtual environment:
    
    pip install pipenv
    pipenv install
    pipenv shell

### Install OpenCV for Python and Utility Libraries

    pipenv install opencv-python
    pipenv install numpy matplotlib imutils

## First OpenCV Example

### Create example file:
    
For example ``CV_Test.py``

Insert following code which displays your default camera stream:

```python
import cv2

exit_chars = [ord("q"), ord("Q"), 27]

win_name = "OpenCV TESTTTTT"


dev_index = 0
capture = cv2.VideoCapture(dev_index)
if not capture.isOpened():
    capture.open(dev_index)

ch = ""

while ch not in exit_chars:
    read, frame = capture.read()
    if read:
        cv2.imshow(win_name, frame)
    
    ch = cv2.waitKey(1) & 0xFF 
```

### Change interpreter:

In Visual Studio Code:
- F1 -> python: select interpreter -> Python \<version\> ('\<folder\>-\<randomID\>')

## Add to github

https://gist.github.com/alexpchin/102854243cd066f8b88e