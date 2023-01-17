import socket
import logging
from threading import Thread

logger = logging.getLogger('server')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('server_logs.log')
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

# IP адреса сервера
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000  # порт, який ми хочемо використовувати
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
logger.info('Server started')

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
             logger.error(f"[!] Error: {e}")
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
    try:
    # постійно відстежувати нові зв'язки
        client_socket, client_addres = s.accept()
        print(f"[+] {client_addres} connected.")
    # додати нового підключеного клієнта до сокетів
        client_sockets.add(client_socket)
        logger.warning('connected: ' + str(client_addres))
    # починаємо новий потік, який прослуховує повідомленния
    # кожного клієнта
        t = Thread(target=listen_for_client, args=(client_socket,))
    # робимо потік демона так, щоб він завершувався кожного разу,
    # коли завершується основний потік
        t.daemon = True
    # почати потік
        t.start()
    except KeyboardInterrupt:
        logging.error('server err: ' + str(KeyboardInterrupt))
        break


# закриваємо клієнтські сокети
for cs in client_sockets:
    cs.close()
# закрити сокет сервера
s.close()