import cv2
import numpy as np
import os

def encode_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Use a simple method like ORB to get descriptors
    orb = cv2.ORB_create()
    _, des = orb.detectAndCompute(image, None)
    
    # Flatten and normalize the descriptors to form a vector
    vector = des.flatten()
    normalized_vector = vector / np.linalg.norm(vector)
    
    return normalized_vector

# Get the script's directory and construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = os.path.join(script_dir, 'Jared-Leto-ProfilePic.webp')

# Get its vector using the encode_image function
vector = encode_image(image_filename)
print(f"Encoded vector for {image_filename}: {vector}")

# Show the image
image_to_display = cv2.imread(image_filename)
cv2.imshow('Image', image_to_display)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  # Close the image window
