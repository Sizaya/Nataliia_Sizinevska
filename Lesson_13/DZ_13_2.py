import random
import time
from statistics import mean
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print('Int list: ', int_list)
print('Float list: ', float_list)
print('Str list: ', str_list)


# Bubble Sort Algorithm
def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    # print('Bubble Sort: ', data)


# bubble_sort(int_list)
# bubble_sort(float_list)
# bubble_sort(str_list)


def average_time(lst, iterance):
    sort_time = []
    for i in range(iterance):
        start_time = time.time()
        bubble_sort(lst)
        contin = time.time() - start_time
        sort_time.append(contin)
    return mean(sort_time)


print(f'Avarange sort time int list: {average_time(int_list, 10)}')
print(f'Avarange sort time float list: {average_time(float_list, 10)}')
print(f'Avarange sort time str list: {average_time(str_list, 10)}')

