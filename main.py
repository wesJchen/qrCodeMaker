import re
import streamlit as st
from PIL import Image

from qrmaker_script import QrMaker
from helpers.style_helper import StyleHelper

# Generate an image using the QrMaker function
qr_instance = QrMaker()

# to be deleted after testing this shiz
img_name = "output/wesley_linkedin_qr.png"
static_test_image = Image.open(img_name)

title_image = Image.open("assets/titleimage.png")
warning_image = Image.open("assets/yeahnosign.png")

### STYLES SETUP ###

st.markdown(
    """
    <style>
    .container-class {
        background-color: white ;
        padding: 15px;
        border-radius: 10px;
        font-family: Menlo;
        text-align: center;
        color: black;
    }
}
    </style>
    """,
    unsafe_allow_html=True,
)

### VARIABLES SETUP ###

# Validate regex of the url link
pattern = r"https://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?"

# Generate containers to separate different areas of the app 
header_container = st.container()
image_container = st.container(border = True)
url_container = st.container(border = True)

### PAGE LAYOUT ###

# Container for the header
with header_container:
    st.markdown('<div class="container-class"><strong>WESLEY\'S QR CODE MAKER</strong></div>',
                unsafe_allow_html=True)
    # st.image(title_image)

    StyleHelper.line_break(1)

# Container for the user URL input
with url_container:
    # Format URL input from user
    title = st.text_input(label="URL Link", placeholder="Enter your url link here", disabled=False)
    if re.fullmatch(pattern,title):
        dynamic_image_byte = qr_instance.qr_save_byte(title)
        st.write("Successfully generated!")
    elif title:
        st.write(f"Fail! The input `{title}`  is not valid. Enter a proper `https://` url.")
    else:
        st.write(" ")

# Container for the image output
with image_container:
    StyleHelper.line_break(2)

    # Format multiple columns on the sheet
    col1, col2, col3 = st.columns(3)
    with col1:
        StyleHelper.line_break(1)

    with col2:
        if re.fullmatch(pattern,title):
            st.image(dynamic_image_byte) #used for the dynamic qr
            # st.image(static_test_image)
        else:
            st.image(warning_image)
    with col3:
        StyleHelper.line_break(1)

    # container footer text
    st.markdown(f"<div style='text-align: center;'><strong>QR link:</strong> <i>{title}</i></div>",
                unsafe_allow_html=True)
    StyleHelper.line_break(3)
