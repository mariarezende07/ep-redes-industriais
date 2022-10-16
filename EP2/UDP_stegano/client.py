import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import socket
from PIL import Image
import io
import os
from utils import reveal_stagnogram, send_byte_array,receive_byte_array_img

dirname = os.path.dirname(__file__)

OUT_IMG = os.path.join(dirname, 'img_secret.png')

HOST = '127.0.0.1'
PORT = 50007

SEG_SIZE = 1022

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    image_path = input("Stegano: ")
    send_byte_array(image_path, s, SEG_SIZE, HOST, PORT)

    msg = input("Secret: ")
    send_byte_array(msg, s, SEG_SIZE, HOST, PORT)

    TOTAL_SIZE = int(s.recvfrom(SEG_SIZE)[0].decode())
    SEG_SIZE = round(TOTAL_SIZE/10)
    
    data = receive_byte_array_img(s, TOTAL_SIZE, SEG_SIZE)[0]
    data = b"".join(data)
    s.close()

img = Image.open(io.BytesIO(data))
img.save(OUT_IMG)
clear_message = reveal_stagnogram(img)


img = mpimg.imread(OUT_IMG)
imgplot = plt.imshow(img)
plt.title("Revealed message: " +clear_message)
plt.show()
