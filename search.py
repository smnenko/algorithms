import math
from random import randrange, choice
from time import time

start_number = 1
stop_number = 1000
numbers_count = 10_000_000
lst = [randrange(start_number, stop_number) for i in range(numbers_count)]
sorted_lst = sorted(lst)


def print_statistics(method: str, spent_time: time, iterations: int):
    print(f'{method} statistics:\n'
          f'    Spent time {spent_time:.8f}s\n'
          f'    Iterations: {iterations}')


def binary_search(sorted_list: list, number: int):
    _start = time()
    low, high = 0, len(sorted_list) - 1
    k = 0

    while low <= high:
        k += 1
        middle = math.ceil((low + high) / 2)
        guess = sorted_lst[middle]
        if guess == number:
            print_statistics('Binary search', time() - _start, k)
            return middle
        elif guess > number:
            high = middle + 1
        else:
            low = middle - 1
    print_statistics('Binary search', time() - _start, k)
    return None


def stupid_search(sorted_list: list, number: int):
    _start = time()
    k = 0
    for index, item in enumerate(sorted_list):
        k += 1
        if item == number:
            print_statistics('Stupid search', time() - _start, k)
            return index
    print_statistics('Binary search', time() - _start, k)
    return None


def python_search(sorted_list: list, number: int):
    _start = time()
    index = sorted_list.index(number)
    print_statistics('Python search', time() - _start, 0)
    return index


if __name__ == '__main__':
    number_what_i_want_to_find = choice(sorted_lst)

    binary_search(sorted_lst, number_what_i_want_to_find)  # O(log n) -> list of 10_000_000 elements may be completed in 24 iterations at worst
    stupid_search(sorted_lst, number_what_i_want_to_find)  # O(n) -> no comments
    python_search(sorted_lst, number_what_i_want_to_find)  # O(n), but it's faster on C language and without k counter
