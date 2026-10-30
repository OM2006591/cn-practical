import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 12345))

s.listen(1)
print("Server is waiting for connection...")

conn, addr = s.accept()
print("Connected to client:", addr)

expression = conn.recv(1024).decode()

a, op, b = expression.split()
a = float(a)
b = float(b)

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Division by zero is not allowed"
else:
    result = "Invalid operator"

conn.send(str(result).encode())

print("Result sent to client:", result)

conn.close()
s.close()
