import cv2

# must have haarcascade_frontalface_alt.xml

def detect(url):
    img = cv2.imread(url)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    rects = face_cascade.detectMultiScale(img, 1.3, 4)
    return img, rects

def mark_face_on(img, rects):
    for (x1, y1, x2, y2) in rects:
        cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (255, 255, 0), 2)
    cv2.imwrite('detected.jpg', img)

img, rects = detect('my2.jpg')
mark_face_on(img, rects)

cv2.imshow('faces',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
