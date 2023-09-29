import cv2 as cv
import os

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '3.jpg')
img = cv.imread(filename)  

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Initialize the SIFT detector
sift = cv.SIFT_create()

# Detect keypoints in the grayscale image
kp = sift.detect(gray, None)

# Draw the keypoints on the original image
img_with_keypoints = cv.drawKeypoints(img, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Save the image with keypoints
cv.imwrite('sift_keypoints.jpg', img_with_keypoints)
