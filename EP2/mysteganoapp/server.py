from stegano import lsb
import os
import matplotlib.pyplot as plt
import socket
import io

dirname = os.path.dirname(__file__)

IN_IMG = os.path.join(dirname, 'img.png')
OUT_IMG = os.path.join(dirname, 'img_secret.png')
msg = 'Hello World'

# 1.1
def steganogram_in_image(IN_IMG, OUT_IMG, msg, plot):

    secret = lsb.hide(IN_IMG, msg)
    secret.save(OUT_IMG)
    if plot:
        image = plt.imread(OUT_IMG)
        plt.imshow(image) 
        plt.show()

        clear_message = lsb.reveal(OUT_IMG)
        print(clear_message)
    return secret



def convert_to_byte_arr(image, format):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()


HOST = '' 
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        img_steg = steganogram_in_image(IN_IMG, OUT_IMG, msg, False)
        img = convert_to_byte_arr(img_steg, 'PNG')
    
        conn.sendall(img)
        
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
