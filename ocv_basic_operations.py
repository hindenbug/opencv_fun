import numpy as np
import cv2


# read/load image using open cv
# imread() - takes two params 'image_path' and 'image reading way' i.e - Color (-1), Grayscale(0),
# Unchanged(1)

# imshow(window_name, image) - displays the image in a window

# load image in color (-1) default
color_img = cv2.imread('test.jpg')
cv2.imshow('color_image', color_img)

# load a grayscale image (0)
gray_img = cv2.imread('test.jpg', 0)
cv2.imshow('gray_image', gray_img)

# load with alpha channel image (1)
un_img = cv2.imread('test.jpg', 1)
cv2.imshow('un_image', un_img)

# waitkey(time) - waits for keyboard event for given time in milliseconds, 0 is waiting forever
cv2.waitKey(0)

# destroyAllWindows() - closes all open windows
cv2.destroyAllWindows()