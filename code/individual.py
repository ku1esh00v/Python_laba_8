#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


if __name__ == '__main__':
    my_tuple = tuple(map(int, input("Enter the elements of the tuple separated by a space: ").split()))

    last_even_index = -1

    for i, (a, b) in enumerate(zip(my_tuple, my_tuple[1:])):
        if a % 2 == 0 and b % 2 == 0:
            last_even_index = i

    if last_even_index != -1:
        temp_result = my_tuple[:last_even_index]
        result = (' '.join(map(str, temp_result)))

        if result == '':
            print('There are no elements before the last pair of adjacent even numbers.')
        else:
            print(result)
    else:
        print("There are no pairs of adjacent even numbers in the tuple!", file=sys.stderr)
