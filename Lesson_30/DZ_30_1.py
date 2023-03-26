class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # реалізація хеш-функції, наприклад:
        return hash(key) % self.size

    def add(self, key, value):
        # додавання елементів в хеш-таблицю
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def remove(self, key):
        # видалення елементів з хеш-таблиці
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return

    def search(self, key):
        # пошук елементів в хеш-таблиці
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def print_table(self):
        # друкування хеш-таблиці
        for index in range(self.size):
            print(index, end=": ")
            for kvp in self.table[index]:
                print(kvp[0], "=", kvp[1], end="; ")
            print()


ht = HashTable(5)
ht.add('apple', 3)
ht.add('banana', 2)
ht.add('orange', 5)
ht.add('peach', 4)
ht.add('grape', 1)

print("Before collision resolution:")
ht.print_table()

ht.add("lemon", 6)

print("After collision resolution:")
ht.print_table()

ht.remove("banana")

print("After removing an element:")
ht.print_table()


print("Searching for an element:")
print(ht.search("apple"))