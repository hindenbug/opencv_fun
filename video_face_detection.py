import cv2

webcam     = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")

while True:
    rval, frame = webcam.read()
    faces = classifier.detectMultiScale(frame)

    for x,y,w,z in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + z), (0, 255, 0), 2)

    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
