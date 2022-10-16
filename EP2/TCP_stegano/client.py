from turtle import clear
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import socket
from PIL import Image, ImageFile
import io
import os
from utils import reveal_stagnogram

dirname = os.path.dirname(__file__)

OUT_IMG = os.path.join(dirname, 'img_secret.png')

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    image_path = input("Stegano: ")
    s.sendall(bytes(image_path,"UTF-8"))

    msg = input("Secret: ")
    s.sendall(bytes(msg,"UTF-8"))
    
    data = s.recv(694773)
    
    s.close()

img = Image.open(io.BytesIO(data))
img.save(OUT_IMG)
clear_message = reveal_stagnogram(img)


img = mpimg.imread(OUT_IMG)
imgplot = plt.imshow(img)
plt.title("Revealed message: " +clear_message)
plt.show()





