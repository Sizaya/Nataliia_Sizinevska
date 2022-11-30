import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55002))
print('[+] Connected.')
message = input('Enter two number separated by commas: ')
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data.decode('utf-8'))
