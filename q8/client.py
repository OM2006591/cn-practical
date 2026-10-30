import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 12345))


expression = input("Enter your expression (e.g. 10 + 5): ")

s.send(expression.encode())

result = s.recv(1024).decode()

print("Result from server:", result)

s.close()
