import DatabaseConnector
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

# Connect to the database
cnx = DatabaseConnector.connect()
cursor = cnx.cursor()

# Retrieve the binary data for the image
query = "SELECT PIC FROM users WHERE USER_ID = %s"
val = ("U000000001",)
cursor.execute(query, val)
result = cursor.fetchone()

# Decode the binary data and create an image object
binary_data = result[0]
image = Image.open(BytesIO(binary_data))

# Convert the image to a format that OpenCV can work with
image_array = np.array(image)
image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

# Display the image
cv2.imshow('image', image_array)
cv2.waitKey(0)

# Close the database connection
cursor.close()
cnx.close()
