import socket
# Create TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to IP address and port
server_socket.bind(('localhost', 12345))

# Listen for client connection
server_socket.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server_socket.accept()
print("Connected to ", addr)

# Receive message from client
message=conn.recv(1024).decode()

# Display message received
print("Message from client: ", message)

# Close connection
conn.close()
server_socket.close()