import pyqrcode

url = str(input('Digite a url para gerar o QrCode: \n'))

qr = pyqrcode.create(url)

qr.png('qrcode.png', scale=8)

