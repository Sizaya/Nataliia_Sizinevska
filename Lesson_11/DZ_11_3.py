import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 65000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    word_count = len(str(data).strip().split(" "))
    print(word_count)
    conn.send(bytes(str(word_count), encoding='UTF-8'))
conn.close()