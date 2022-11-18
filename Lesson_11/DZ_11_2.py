import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 60000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    if str(data) == "b'start'":
        data = b'Start process'
        conn.send(data)
    if str(data) == "b'read'":
        data = b'Read article'
        conn.send(data)
    if str(data) == "b'finish'":
        data = b'Goodbye'
        conn.send(data)
    else:
        conn.send(data)
conn.close()