#!/usr/bin/env python

import unittest


def print_backwards(n):
    if n == 0:
        print(n)
        return
    print(n)
    print_backwards(n-1)


class TestPrintBackwards(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_print_backwards(self):
        n = 5
        print_backwards(n)


if __name__ == '__main__':
    unittest.main()
