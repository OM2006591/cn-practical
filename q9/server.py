import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('localhost', 12345))

print("Server is waiting for client...")

data, address = server.recvfrom(1024)

message = data.decode()

print("Received from client:", message)

converted = message.upper()

server.sendto(converted.encode(), address)

print("Converted string sent:", converted)
