import numpy as np
import cv2 as cv
import os

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '3.jpg')
img = cv.imread(filename)
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('sift_keypoints.jpg',img)