#!/usr/bin/env python

import unittest


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class TestFibonacci(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fibonacci(self):
        n = 10
        fibs_groundtruth = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for ii in range(n):
            self.assertEqual(fibs_groundtruth[ii], fibonacci(ii))


if __name__ == '__main__':
    unittest.main()

