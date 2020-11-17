#!/usr/bin/env python

import unittest


def print_recursive(arr):
    """
    Recursively print an array

    """
    # print(arr)
    if len(arr) == 1:
        print(arr[0])
    else:
        print_recursive([arr[0]])
        # print(arr[0])
        print_recursive(arr[1:])


class TestPrint(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = range(10)

    def test_print(self):
        print_recursive(self.arr)


if __name__ == '__main__':
    unittest.main()