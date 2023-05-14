""" 
# QR code project

# AC:
    # verify the website link provided is valid
    # verify the qr code capture directs to the site provided url
    # verify the qr code is a clear format and not blurry upon file save
    # verify save and exporting qr code as png file

# nice to haves:
    #designs to implement along the qr code image graphic
    #analytic for qr code captures and tracking e.g. GA

ref: https://pypi.org/project/qrcode/
"""

import qrcode
import sys, os
from qrcode import constants
from PIL import Image, ImageDraw

#contains the qr library to create qr code as PNG
class QR_maker():

#define the size and border of the box
    def __init__(self):
        self.size = 10
        self.border = 2
        self.folder_path = "qr_images"

#create the qr code with method
    def qr_save(self, url, file_name):
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
        draw = ImageDraw.Draw(image_file)

        border_width = 4
        #custom styling added below
        draw.rectangle(xy=[(0,0),
                           (image_file.size[0] - 1, image_file.size[1] - 1)],
                           outline = 'black',
                           width=border_width)
 
        #save the file
        os.makedirs(self.folder_path, exist_ok=True)
        image_path = f"{self.folder_path}/{file_name}.png"
        image_file.save(image_path)


if __name__ == "__main__":
    #store arguments after the script filename / index pos 0 from the CL
    if len(sys.argv) <3:
        print("Provide the URL and file name as CL arguments")
        sys.exit(1)

    qrMachine = QR_maker()
    url = sys.argv[1]
    file_name = sys.argv[2]
    qrMachine.qr_save(url, file_name)
    print(f"File image for website '{url}': CREATED as '{file_name}.png'")