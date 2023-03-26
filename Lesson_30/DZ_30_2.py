import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class AuthTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add_user(self, user):
        index = self.hash_function(user.username)
        for u in self.table[index]:
            if u.username == user.username:
                raise ValueError("Користувач з таким ім'ям вже існує")
        self.table[index].append(user)

    def verify_user(self, username, password):
        index = self.hash_function(username)
        for u in self.table[index]:
            if u.username == username and u.password == hashlib.sha256(password.encode()).hexdigest():
                return True
        return False

    def interactive_login(self):
        username = input("Ім'я користувача: ")
        password = input("Пароль: ")
        if self.verify_user(username, password):
            print("Авторизація успішна")
        else:
            print("Невірні ім'я або пароль")


auth_table = AuthTable(5)

user1 = User("Nata", "pass1")
user2 = User("Den", "pass2")
user3 = User("Roma", "pass3")

auth_table.add_user(user1)
auth_table.add_user(user2)
auth_table.add_user(user3)

auth_table.interactive_login()
