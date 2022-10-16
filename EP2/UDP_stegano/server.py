import socket
from utils import steganogram_image, convert_to_byte_arr,receive_byte_array, send_byte_array_img, send_byte_array
import os

dirname = os.path.dirname(__file__)

HOST = '' 
PORT = 50007

SEG_SIZE = 1022
TOTAL_SIZE = 694960

s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    print("Now listening...\n")
    
    while True:
        
        img_path = receive_byte_array(s, TOTAL_SIZE, SEG_SIZE)[0][0].decode()
        msg, addr = receive_byte_array(s, TOTAL_SIZE, SEG_SIZE)

        msg = msg[0].decode()
        if not img_path or not msg: 
            break

        IN_IMG = os.path.join(dirname, img_path)
        image = steganogram_image(IN_IMG, msg)
        bit_img = convert_to_byte_arr(image, 'PNG')
        img_size = str(len(bit_img))
        s.sendto(bytes(img_size,"UTF-8"), addr)

        send_byte_array_img(bit_img, s, SEG_SIZE, addr[0], addr[1])
            
        print("All sended")
        break

