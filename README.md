# qrCodeMaker
Allow user to generate a static QR code files for websites with any URL.


# Description
The file contains a simple object that will generate a QR code for the user as long as a valid url and file name is input. This can be used to demonstrate a particular website for quick and easy access with the snap of the camera on a mobile device.

Project contains several sample QR codes generated for my personal links. They are stored in default created qr_images folder

# Usage
1. Clone the git repo and install the dependencies.
2. Run the qrmaker.py file passing in the following arguments:
"""
:param website_url: website of the URL you want to create an image of
:param qr_image_name: image file name that will be saved

`PYTHONPATH=. python3 qrmaker_script.py <website_url> <qr_image_name>`

"""

Output:
- The file can be run on a CLI by taking in two arguments.
- As long as the user provides a url link and file name as string values, they will be passed as arguments and generate a file in a folder within this project
- A png file is then generated for the QR code (static) which can be downloaded saved onto your local machine.

# Contact
Questions directed at wesjchen@gmail.com

# Reception
Potentially adding FE app to generate the QR code for a better UX.
