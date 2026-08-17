import qrcode

url = input("Enter the Url: ")
file_path = "C:\\Users\\dewas\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Qr code was generated!! ")