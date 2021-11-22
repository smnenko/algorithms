from random import randrange
from time import time

from binary_search import print_statistics


start_number = 1
stop_number = 100
numbers_count = 5_000
lst = [randrange(start_number, stop_number) for i in range(numbers_count)]


def get_smallest_index(unsorted_list: list):
    smallest = unsorted_list[0]
    smallest_index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] <= smallest:
            smallest = unsorted_list[i]
            smallest_index = i
    return smallest_index


def choice_sort(unsorted_list: list):
    _start = time()
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest_item = get_smallest_index(unsorted_list)
        sorted_list.append(unsorted_list.pop(smallest_item))
    print_statistics('Choice sort', time() - _start, 0)
    return sorted_list


if __name__ == '__main__':
    choice_sort(lst)
