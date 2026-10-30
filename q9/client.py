import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter a lowercase string: ")

client.sendto(message.encode(), ('localhost', 12345))

data, address = client.recvfrom(1024)

print("Uppercase string received from server:", data.decode())

client.close()
