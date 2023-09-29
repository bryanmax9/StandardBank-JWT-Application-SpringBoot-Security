import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '5.jpg')
img = cv.imread(filename, cv.IMREAD_GRAYSCALE)

# Initiate STAR detector with adjusted parameters
star = cv.xfeatures2d.StarDetector_create()
star.setMaxSize(15)  # Adjust this parameter
star.setResponseThreshold(30)  # Adjust this parameter

# Initiate BRIEF extractor
brief = cv.xfeatures2d.BriefDescriptorExtractor_create()

# Find the keypoints with STAR
kp = star.detect(img, None)

if kp:
    # Compute the descriptors with BRIEF
    kp, des = brief.compute(img, kp)
    print(brief.descriptorSize())
    if des is not None:
        print(des.shape)
    else:
        print("No descriptors were computed.")
else:
    print("No keypoints were found.")
