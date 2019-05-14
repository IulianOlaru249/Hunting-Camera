import socket
HOST = '192.168.86.110'
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
except Exception as e:
    print("Cannot connect to the server:", e)
print("Connected")
