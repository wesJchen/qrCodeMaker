"""
TO DO:
* Implement a bytes buffer for the image to be stored as

"""

#SAMPLE CODE
import streamlit as st
import io
from PIL import Image
import numpy as np

# Create a bytes buffer for the image
img_buffer = io.BytesIO()

# Example: Create a simple image using PIL or numpy
# (Replace this with your actual image data)
img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
img = Image.fromarray(img_array)

# Save the image to the buffer
img.save(img_buffer, format='PNG')
img_bytes = img_buffer.getvalue()

# Display the image directly from bytes
st.image(img_bytes)


# # If you already have image bytes
# image_bytes = your_image_bytes  # Your bytes data here
# st.image(image_bytes)