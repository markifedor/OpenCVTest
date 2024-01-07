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