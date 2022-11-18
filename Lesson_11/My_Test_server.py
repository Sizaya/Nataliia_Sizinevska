import socket
from threading import Thread

# IP адреса сервера
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5002  # порт, який ми хочемо використовувати
separator_token = "<SEP>"   # для розділення імені клієнта та повідомлення

# ініціалізуємо список усіх підключених сокетів клієнта
client_sockets = set()
# створюємо сокет TCP
s = socket.socket()
# робимо порт багаторазовим
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# прив'язуємо сокет до вказаної нами адреси
s.bind((SERVER_HOST, SERVER_PORT))
# частота прослуховування майбутніх підключень
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    """"
    Ця функція прослуховує повідомлення з сокета.
    Щоразу, коли надходять повідомлення, транслює його
    всім іншим підключеним клієнтам.
    """
    global client_socket, msg
    while True:
        try:
            # слухаємо повідомлення з сокета 'cs'
            msg = cs.recv(1024).decode()
        except Exception as e:
            #якщо клієнт не підключений видалити його
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # якщо отримуємо повідомлення замінюємо <SEP>
            # маркер ":" для гарного виводу
            msg = msg.replace(separator_token, ": ")
            # повторити всі підключені сокети
        for client_socket in client_sockets:
            # надіслати повідомлення
            client_socket.send(msg.encode())

while True:
    # постійно відстежувати нові зв'язки
    client_socket, client_addres = s.accept()
    print(f"[+] {client_addres} connected.")
    # додати нового підключеного клієнта до сокетів
    client_sockets.add(client_socket)
    # починаємо новий потік, який прослуховує повідомленния
    # кожного клієнта
    t = Thread(target=listen_for_client, args=(client_socket,))
    # робимо потік демона так, щоб він завершувався кожного разу,
    # коли завершується основний потік
    t.daemon = True
    # почати потік
    t.start()
# закриваємо клієнтські сокети
for cs in client_sockets:
    cs.close()
# закрити сокет сервера
s.close()