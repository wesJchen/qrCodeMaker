import streamlit as st
from PIL import Image

from qrmaker_script import QrMaker
from helpers.style_helper import StyleHelper

# Generate an image using the QrMaker function
# qr_instance = QrMaker()
# img_bytes = qr_instance.qr_save_byte("www.target.com")

# to be deleted after testing this shiz
img_name = "output/wesley_linkedin_qr.png"
static_test_image = Image.open(img_name)

# #Load the CSS Styles
# StyleHelper.load_css("styles.css") #nevermind :<

st.markdown(
    """
    <style>
    .container-class {
        background-color: #6a0dad ;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Generate containers to separate different areas of the app 
header_container = st.container()
container = st.container(border = True)

with header_container:
    st.markdown('<div class="container-class">QR Image Maker</div>', unsafe_allow_html=True)
    StyleHelper.line_break(1)

with container:

    StyleHelper.line_break(5)

    # Format multiple columns on the sheet
    col1, col2, col3 = st.columns(3)
    with col1:
        StyleHelper.line_break(1)

    with col2:
        st.image(static_test_image)
        StyleHelper.line_break(5)

    with col3:
        StyleHelper.line_break(1)
    # st.image(static_test_image)

StyleHelper.line_break(3)

# Format URL input from user
title = st.text_input(label="URL Link", placeholder="Paste url link here", disabled=True)
if title:
    st.write("QR has been generated for", title)
else:
    st.write(" ")

# #Input the bytes of the QR image generated
# st.image(img_bytes)