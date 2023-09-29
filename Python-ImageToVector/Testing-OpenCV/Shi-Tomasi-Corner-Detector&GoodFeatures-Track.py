import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

import os

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '2.jpg')
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()