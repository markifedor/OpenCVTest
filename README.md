# OpenCV

## Install Pip Environment
make folder:

    mkdir <folder>

Go to folder:

    cd <folder>

Make virtual environment:
    
    pip install pipenv
    pipenv install
    pipenv shell

## Install OpenCV for Python and Utility Libraries

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

