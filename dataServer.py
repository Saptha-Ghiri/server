
import socket
import threading
import time
def data_ser(port,ip):
    # Client function for sending data to the server
    def client_send(server_socket):
        while True:
            message = input()
            server_socket.send(message.encode())
            

    # Client function for receiving data from the server
    def client_receive(server_socket):
        while True:
            data = server_socket.recv(1024)
            print("Server (Received): " + data.decode())

    # Client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    # Create and start client threads
    client_send_thread = threading.Thread(target=client_send, args=(client_socket,))
    client_receive_thread = threading.Thread(target=client_receive, args=(client_socket,))
    client_send_thread.start()
    client_receive_thread.start()

