import random
import socket
from datetime import datetime
from threading import Thread

from colorama import Fore, init, Back

# кольори
init()
# встановлюємо доступні кольори
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLACK_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE,
          Fore.YELLOW]
# вибір випадкового кольору для клієнта
client_color = random.choice(colors)
# вказуємо IP сервера
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000  # порт сервера
separator_token = "<SEP>"   # для розділення імені клієнта і повідомлення
# ініціалізація сокета TCP
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}: {SERVER_PORT}...")
# підключення до сервера
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
# запитати у клієнта ім'я
name = input("Enter your name: ")

def listen_for_massages():
    """
    Ця функція прослуховує повідомлення з сервера
    та виводить іх у консоль.
    """
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)
# потік, який прослуховує повідомлення для цього клієнта
# і друкує їх
t = Thread(target=listen_for_massages)
# робимо потік демона, так щоб він завершувався кожного разу,
# коли завершується основний потік
t.daemon = True
# почати потік
t.start()

while True:
    # вхідне повідомлення, яке надсилається на сервер
    to_send = input()
    # спосіб виходу з програми
    if to_send.lower() == '/q':
        break
    # дата, час, ім'я та колір відправника
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}]{name}{separator_token}{to_send}{Fore.RESET}"
    # надіслати повідомлення
    s.send(to_send.encode())
# закрити сокет
s.close()
