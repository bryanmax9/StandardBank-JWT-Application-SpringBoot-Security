import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'kirby.webp')
filename2 = os.path.join(script_dir, 'kirby-InScene.webp')

img1 = cv.imread(filename, cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread(filename2, cv.IMREAD_GRAYSCALE)         # trainImage

# Initiate ORB detector with adjusted parameters
orb = cv.ORB_create(nfeatures=500, scaleFactor=1.2, nlevels=8)

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Check if keypoints were found
if kp1 and kp2:
    print("Keypoints found in both images.")
else:
    print("No keypoints were found in one or both images.")

# You can now proceed with matching the descriptors or performing further analysis.
