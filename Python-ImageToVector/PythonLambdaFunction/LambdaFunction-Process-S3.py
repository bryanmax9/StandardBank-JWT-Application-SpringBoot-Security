import boto3  # AWS SDK for Python. Used for interacting with AWS services.
import cv2  # OpenCV library, used for computer vision tasks.
import numpy as np  # NumPy library, used for numerical operations on arrays.

# Initialize the AWS S3 client. This allows the script to communicate with the S3 service.
s3_client = boto3.client('s3')

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def encode_image_from_np_array(np_array):
  """
  Encode an image (represented as a numpy array) into a vector using OpenCV.

  Args:
  - np_array (numpy.ndarray): The image data in numpy array format.

  Returns:
  - numpy.ndarray: A normalized vector representation of the image.
  """
  # Convert the numpy array to an image in grayscale.
  # Grayscale is used to simplify the image and only keep luminance information.
  image = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    
  # Detect faces in the grayscale image
  faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
  # If no faces are detected, return an empty list
  if len(faces) == 0:
    return []
    
  # For this example, we'll just use the first detected face
  (x, y, w, h) = faces[0]
  face_region = image[y:y+h, x:x+w]
    
  orb = cv2.ORB_create()
  _, des = orb.detectAndCompute(face_region, None)
   
  vector = des.flatten()
  normalized_vector = vector / np.linalg.norm(vector)
    
  return normalized_vector

def lambda_handler(event, context):
  """
  AWS Lambda function to process an image from S3, encode it, and return the encoded vector.

  Args:
  - event (dict): Contains information about the triggering event. In this case, details about the S3 object.
  - context (LambdaContext): Provides methods and properties that provide information about the invocation, 
                              function, and execution environment.

  Returns:
  - dict: A response object with a status and the encoded image vector.
  """
  # Extract the name of the S3 bucket and the file key (path) from the triggering event.
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  file_key = event['Records'][0]['s3']['object']['key']

  # Use the S3 client to retrieve the file object from the specified bucket and path.
  s3_file = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    
  # The actual image data is stored in the 'Body' of this object.
  # Read it and convert it to a numpy array for processing.
  image_data = s3_file['Body'].read()
  np_array = np.frombuffer(image_data, np.uint8)
    
  # Use the previously defined function to encode this image into a vector.
  encoded_vector = encode_image_from_np_array(np_array)
    
  # Return a response object. This could be further sent to another service or stored in a database.
  return {
    'statusCode': 200,  # A standard HTTP response to indicate success.
    'body': encoded_vector.tolist()  # Convert the numpy array to a list for JSON serialization.
  }
