import io
import qrcode
import sys, os
from qrcode import constants
from PIL import ImageDraw

from modules.enums import ImgFileExt

#contains the qr library to create qr code as PNG
class QrMaker:

    def __init__(self):
        self.size = 10
        self.border = 2
        self.folder_path = "qr_images"

    def qr_save_local(self, url:str, file:str) -> None:
        """
        Generate a qr code provided a URL of the site and a file name to save as.

        :param url: str of the URL
        :param file: name of the file provided
        :return: None
        """
        ### ARRANGE ###
        border_width = 0

        ### ACT ###

        qr = qrcode.QRCode(
            version=1,
            error_correction = constants.ERROR_CORRECT_L,
            box_size = self.size,
            border = self.border
            )
        qr.add_data(url)
        qr.make(fit=True)
        image_file = qr.make_image(fill_color = "black",
                                   back_color = "white") #back_color=(255,195,235)
        
        # Creating a draw object to modify the existing QR image.
        draw = ImageDraw.Draw(image_file)
        draw.rectangle(xy=[(0,0),
                           (image_file.size[0] - 1, image_file.size[1] - 1)],
                           outline = 'black',
                           width=border_width)

        #Save file as a PNG
        os.makedirs(self.folder_path, exist_ok=True)
        image_path = f"{self.folder_path}/{file}.{ImgFileExt.PNG.value}"
        image_file.save(image_path)

    def qr_save_byte(self, url:str) -> bytes:
        """
        Generate a QR code saved as bytes to be returned. This will be used by the streamlit UI upon deploy.

        :param url: str of the QR code to be generated
        :return: Return the bytes of the PNG file
        """
        ### ARRANGE ###
        img_buffer = io.BytesIO()

        ### ACT ###
        img = qrcode.QRCode(
                version=1,
                error_correction = constants.ERROR_CORRECT_L,
                box_size = self.size,
                border = self.border
            )
        img.add_data(url)
        img.make(fit=True)
        
        image_file = img.make_image(fill_color = "black",
                                    back_color = "white") #back_color=(255,195,235)

        # Save the image to the buffer
        image_file.save(img_buffer, format={ImgFileExt.PNG.value})
        img_bytes = img_buffer.getvalue()

        return img_bytes

if __name__ == "__main__":
    #store arguments after the script filename / index pos 0 from the CL
    if len(sys.argv) <3:
        print("Provide the URL and file name as CL arguments, e.g. google.com, google_qr")
        sys.exit(1)

    qr_machine = QrMaker()
    url = sys.argv[1]
    file = sys.argv[2]
    qr_machine.qr_save_local(url=url, file=file)
    print(f"File image for website '{url}': CREATED as '{file}.png'")