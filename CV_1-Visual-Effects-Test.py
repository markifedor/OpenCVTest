import cv2
import numpy as np

NORMAL = 0  # Preview Mode
BLUR = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY = 3  # Canny Edge Detector

feature_params = dict(
    maxCorners = 500,
    qualityLevel = 0.2,
    minDistance = 15,
    blockSize = 9
    )

NO_FLIP = None
FLIP_HORIZONTAL = 1
FLIP_VERTICAL = 0
FLIP_ON_BOTH_AXES = -1
FLIP_ARRAY = [NO_FLIP, FLIP_HORIZONTAL, FLIP_VERTICAL, FLIP_ON_BOTH_AXES]

flip = NO_FLIP
f_index = 0

DEFAULT_COLOR_MODE = 0
COLOR_MODES_ARRAY = [DEFAULT_COLOR_MODE, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2GRAY]

cm = DEFAULT_COLOR_MODE
cm_index = 0

image_filter = NORMAL

exit_chars = [ord("q"), ord("Q"), 27]

win_name = "OpenCV TESTTTTT"


dev_index = 0
capture = cv2.VideoCapture(dev_index)
if not capture.isOpened():
    capture.open(dev_index)

ch = ""

while ch not in exit_chars:

    read, frame = capture.read()  
    result = frame

    if read:

        if flip != NO_FLIP:
            result = cv2.flip(result, flip)
    
        if cm != DEFAULT_COLOR_MODE:
            if image_filter != FEATURES:
                result = cv2.cvtColor(result, cm)

        if image_filter == CANNY:
            # Applying Canny Edge Detect Filter
            result = cv2.Canny(result, 80, 200)

        elif image_filter == BLUR:
            # Applying Blur Filter
            result = cv2.blur(result, (40, 40))

        elif image_filter == FEATURES:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
            
            if corners is not None:
                for x, y in np.float32(corners).reshape(-1, 2):
                    cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)
        
        # Do nothing if image_filter is NORMAL
                    
        cv2.imshow(win_name, result)
        
    ch = cv2.waitKey(1) & 0xFF

    if ch == ord("E") or ch == ord("e"): # e for "edges"
        image_filter = CANNY

    elif ch == ord("B") or ch == ord("b"): # b for "blur"
        image_filter = BLUR

    elif ch == ord("C") or ch == ord("c"): # c for "corners"
        image_filter = FEATURES

    elif ch == ord("F") or ch == ord("f"): # f for "flip"
        f_index += 1
        f_index &= 3
        flip = FLIP_ARRAY[f_index]

    elif ch == ord("M") or ch == ord("m"): # m for "color _M_ode"
        if image_filter != FEATURES:
            cm_index += 1
            cm_index &= 3
            cm = COLOR_MODES_ARRAY[cm_index]

    elif ch == ord("N") or ch == ord("n"): # n for "normal"
        image_filter = NORMAL

        cm_index = DEFAULT_COLOR_MODE
        cm = COLOR_MODES_ARRAY[cm_index]

        f_index = 0
        flip = FLIP_ARRAY[f_index]
capture.release()
cv2.destroyAllWindows()