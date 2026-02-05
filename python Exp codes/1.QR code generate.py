import qrcode

url = input("enter url: ").strip()

file_path = "/home/aditya/Downloads/ALL PROGRAMMING/python programming (youtube)/first python program/qrcode_image.png"

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(file_path)

print("qrcode generated!")
