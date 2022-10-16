import matplotlib.pyplot as plt
import socket

import socket
HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    s.sendall(b"Received")
    
    data = s.recv(1024)
    
    s.close()

print(data)
