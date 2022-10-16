import matplotlib.pyplot as plt
import socket
from PIL import Image, ImageFile
import io
import socket

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    s.sendall(b"Received")
    
    data = s.recv(694773)
    
    s.close()

img = Image.open(io.BytesIO(data))
img.show()





