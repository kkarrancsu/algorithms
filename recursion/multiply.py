#!/usr/bin/env python

import unittest


def multiply(a, b):
    """
    computes a*b recursively.
    recall, a*b = sum(a, i=0, b-1) times
    """
    if b == 1:
        return a
    return multiply(a, b-1) + a


class TestMultiply(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_multiply(self):
        a = 4
        b = 8
        multiply_expect = a*b
        multiply_actual = multiply(a,b)
        self.assertEqual(multiply_expect, multiply_actual)


if __name__ == '__main__':
    unittest.main()