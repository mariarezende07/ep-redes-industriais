import socket
from utils import steganogram_image, convert_to_byte_arr 
import os

dirname = os.path.dirname(__file__)

IN_IMG = os.path.join(dirname, 'img.png')
msg = 'Hello World'

HOST = '' 
PORT = 50007
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    print("Now listening...\n")
    image = steganogram_image(IN_IMG, msg)
    bit_img = convert_to_byte_arr(image, 'PNG')

    socket_size = len(bit_img)
    print(socket_size)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        
        data = conn.recv(socket_size)
        if not data: 
            break
        
        
        conn.sendall(bit_img)
        print(data)
        break
