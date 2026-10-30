import socket
# Create TCP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))

# Enter message 
message=input("Enter a message: ")

# Send message to sever
client_socket.send(message.encode())
print("Message sent successfully!")

# Close connection
client_socket.close()