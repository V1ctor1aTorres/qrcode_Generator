import pyqrcode
#Funcionalidades para criar códigos QR em Python

url = str(input('Digite a url para gerar o QrCode: \n'))
#Usa a função create para criar um objeto QR Code com a URL fornecida
qr = pyqrcode.create(url)
#Usa o método png do objeto qr para gerar uma imagem do QR Code e salvá-la 
#O parâmetro scale define o tamanho do bloco de pixels no QR Code
qr.png('qrcode.png', scale=8)

