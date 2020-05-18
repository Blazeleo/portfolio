import pyqrcode
import re


# Generate QR
def Gen():
    name = input("Enter the text\n").strip()
    fileName = input("Enter the name of the file (with extension)\n").strip()

    qr = pyqrcode.create(name)
    qr.png(fileName, scale=8)


# Read QRcode
def Read():
    from pyzbar.pyzbar import decode
    from PIL import Image

    name = input("Enter the file name (with extension)\n").strip()

    d = decode(Image.open(name))

    print(d[0].data.decode('ascii'))


def main():
    inp = input("Generate (1) or Read (2) QR code?\n").strip()

    if inp == '1':
        Gen()

    elif inp == '2':
        Read()

    else:
        print("Wrong input format. Input 1 or 2")
        main()


if __name__ == "__main__":
    main()
