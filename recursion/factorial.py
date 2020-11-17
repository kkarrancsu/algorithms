#!/usr/bin/env python

import unittest


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


class TestFactorial(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_factorial(self):
        n = 5
        factorial_expect = 1
        for ii in range(n, 0, -1):
            factorial_expect *= ii
        factorial_actual = factorial(n)
        self.assertEqual(factorial_expect, factorial_actual)


if __name__ == '__main__':
    unittest.main()