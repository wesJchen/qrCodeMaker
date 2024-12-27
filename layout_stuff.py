"""
TO DO:
* Implement a bytes buffer for the image to be stored as

"""

#SAMPLE CODE
import streamlit as st
from qrmaker_script import QrMaker

qr_instance = QrMaker.qr_save_local

image_bytes = your_image_bytes  # Your bytes data here
st.image(image_bytes)
