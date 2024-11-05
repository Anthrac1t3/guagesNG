import socket
import time

if __name__ == 'main':
    client_socket = client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect('localhost', 4444)
    client_socket.accept()