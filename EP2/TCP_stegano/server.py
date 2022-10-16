import socket
from utils import steganogram_image, convert_to_byte_arr 
import os

dirname = os.path.dirname(__file__)

HOST = '' 
PORT = 50007
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    print("Now listening...\n")
    

    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        
        img_path = conn.recv(694773).decode()
        msg = conn.recv(694773).decode()

        if not img_path or not msg: 
            break

        print(img_path, msg)
        IN_IMG = os.path.join(dirname, img_path)
        image = steganogram_image(IN_IMG, msg)
        bit_img = convert_to_byte_arr(image, 'PNG')
        
        conn.sendall(bit_img)
        break

