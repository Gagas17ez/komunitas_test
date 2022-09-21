import numpy as np
import cv2 

 # Load an color image in grayscale
img = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

 # show image
cv2.imshow('image normal',img)
cv2.waitKey(0)
cv2.destroyAllWindows()