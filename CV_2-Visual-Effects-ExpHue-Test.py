import cv2
import numpy as np

NORMAL = 0  # Normal image

DARKER = -1
BRIGHTER = 1

LOW_CONTRAST = -2
HIGH_CONTRAST = 2

DEFAULT_COLOR_MODE = 0
COLOR_MODES_ARRAY = [DEFAULT_COLOR_MODE, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2GRAY]

cm = DEFAULT_COLOR_MODE
cm_index = 0

image_filter = NORMAL

exit_chars = [ord("q"), ord("Q"), 27]

win_name = "OpenCV TESTTTTT"

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
FRAME_PARAMETERS = (IMAGE_HEIGHT, IMAGE_WIDTH, 3)

brightness_matrix = np.ones(FRAME_PARAMETERS, dtype = "uint8") * 50
contrast_matrix_low = np.ones(FRAME_PARAMETERS, dtype = "uint8") * 0.6
contrast_matrix_high = np.ones(FRAME_PARAMETERS, dtype = "uint8") * 1.6


dev_index = 0
capture = cv2.VideoCapture(dev_index)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)

if not capture.isOpened():
    capture.open(dev_index)

ch = ""

while ch not in exit_chars:

    read, frame = capture.read()

    if cm != DEFAULT_COLOR_MODE:
        frame = cv2.cvtColor(frame, cm)

    if read:
        if cm == cv2.COLOR_BGR2GRAY:
            image_filter = NORMAL
        if image_filter == NORMAL:
            frame = frame
        elif image_filter == BRIGHTER:
            frame = cv2.add(frame, brightness_matrix)
        elif image_filter == DARKER:
            frame = cv2.subtract(frame, brightness_matrix)
        elif image_filter == LOW_CONTRAST:
            frame = np.uint8(cv2.multiply(np.float64(frame), contrast_matrix_low))
        elif image_filter == HIGH_CONTRAST:
            frame = np.uint8(np.clip(cv2.multiply(np.float64(frame), contrast_matrix_high), 0, 255))

        cv2.imshow(win_name, frame)
        
    ch = cv2.waitKey(1) & 0xFF



    if ch == ord("M") or ch == ord("m"): # m for "color _M_ode"
        cm_index += 1
        cm_index &= 3
        cm = COLOR_MODES_ARRAY[cm_index]

    elif ch == ord("B") or ch == ord("b"): # b for "brighter"
        image_filter = BRIGHTER
    elif ch == ord("D") or ch == ord("d"): # d for "darker"
        image_filter = DARKER

    elif ch == ord("H") or ch == ord("h"): # h for "high contrast"
        image_filter = HIGH_CONTRAST
    elif ch == ord("L") or ch == ord("l"): # l for "low contrast"
        image_filter = LOW_CONTRAST

    elif ch == ord("N") or ch == ord("n"): # n for "normal"
        image_filter = NORMAL

        cm_index = DEFAULT_COLOR_MODE
        cm = COLOR_MODES_ARRAY[cm_index]
        
capture.release()
cv2.destroyAllWindows()