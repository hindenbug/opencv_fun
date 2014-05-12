import cv2

# initialize VideoCapture object

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    # returns True/False and the next frame
    rval, frame = webcam.read()
else:
    rval = False

while rval:
    cv2.imshow('preview', frame)
    rval, frame = webcam.read()
    key = cv2.waitKey(10)
    if key == 27:    # Esc key to stop
        break
