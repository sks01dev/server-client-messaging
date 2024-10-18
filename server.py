import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP and port
ip = "127.0.0.1"
port = 5566
server_socket.bind((ip, port))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port", port)

# Accept a connection from a client
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Infinite loop to receive and send messages
while True:
    # Receive message from the client
    recv_msg = client_socket.recv(1024).decode()
    print(f"Client: {recv_msg}")

    # Input message from user to send to the client
    msg = input("Enter message to send: ")
    client_socket.send(msg.encode())
