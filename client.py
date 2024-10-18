import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP and Port
ip = "127.0.0.1"
port = 5566

# Connecting to the server
s.connect((ip, port))
print("Connected to the server!")

# Infinite loop to receive and send messages
while True:
    # Input message from user to send to the server
    msg = input("Enter Your Message: ")
    s.send(msg.encode())

    # Receive message from the server
    recv_msg = s.recv(1024).decode()
    print(f"Server: {recv_msg}")
