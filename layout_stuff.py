"""
TO DO:
* Implement a bytes buffer for the image to be stored as

"""
import streamlit as st
from qrmaker_script import QrMaker

qr_instance = QrMaker()
img_bytes = qr_instance.qr_save_byte("www.target.com")

#Input the bytes of the QR image generated
st.image(img_bytes)
