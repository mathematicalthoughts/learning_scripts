import string
import qrcode
import random

def generate_random_name():
    alphabet = list(string.ascii_letters)
    file_name = []
    for i in range(13):
        file_name.append(random.choice(alphabet))
    return ("".join(file_name))

r_file_name = generate_random_name()

img_source = input("Enter a string to generate a QR Code: ")

img_qr_code = qrcode.make(img_source)

img_file = open(f'{r_file_name}.png','wb')

img_qr_code.save(img_file)
img_file.close
