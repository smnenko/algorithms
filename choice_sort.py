import math
from random import randrange
from time import time

from binary_search import print_statistics


start_number = 1
stop_number = 100
numbers_count = 5_000
lst = [randrange(start_number, stop_number) for i in range(numbers_count)]
lst_copy = lst[:]
k = 0


def get_smallest_index(unsorted_list: list):
    smallest = unsorted_list[0]
    smallest_index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] <= smallest:
            smallest = unsorted_list[i]
            smallest_index = i
    return smallest_index


def choice_sort(unsorted_list: list):
    k = 0
    _start = time()
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest_item = get_smallest_index(unsorted_list)
        sorted_list.append(unsorted_list.pop(smallest_item))
        k += 2
    print_statistics('Choice sort', time() - _start, k)
    return sorted_list


def quick_sort(unsorted_list: list):
    global k
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        avg_index = math.ceil(len(unsorted_list) / 2)
        base_num = unsorted_list[avg_index]
        less_num = [
            i
            for i in unsorted_list[1:avg_index] + unsorted_list[avg_index:]
            if i <= base_num
        ]
        greater_num = [
            i
            for i in unsorted_list[1:avg_index] + unsorted_list[avg_index:]
            if i > base_num
        ]
        k += 2
        return quick_sort(less_num) + [base_num] + quick_sort(greater_num)


def call_quick_sort(unsorted_list: list):
    _start = time()
    quick_sort(unsorted_list)
    print_statistics('Quick sort', time() - _start, k)


def python_sort(unsorted_list: list):
    _start = time()
    result = sorted(unsorted_list)
    print_statistics('Python sort', time() - _start, 0)
    return result


if __name__ == '__main__':
    choice_sort(lst)
    call_quick_sort(lst_copy)
    python_sort(lst_copy)
