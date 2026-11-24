import qrcode

url = input("url : ")

image = qrcode.make(url)

image.save("image.png")
