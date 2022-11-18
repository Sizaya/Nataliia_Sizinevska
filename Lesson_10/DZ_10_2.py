import sys

def unique_numbers(*num):
    try:
        set_num = set(num)
        if len(num) == len(set_num):
            print("Numbers are unique")
        else:
            print("Same numbers")
    except TypeError as te:
        print(f'{te}, use only tuples, sets, strings and numbers', file=sys.stderr)


unique_numbers([1, 2, 3, 4])
unique_numbers(1, 2, 3, 4, 5)
unique_numbers(1, 2, 3, 4, 5, 5)
