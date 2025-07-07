#QR Code Generator In Python 
import qrcode as qr

img = qr.make(input("Enter Your Genrate QRcode URL:  "))

img.save("qrcode.png")