#!/usr/bin/env python

import unittest


def summer(n):
    """
    Computes 1+2+...+n
    """
    if n == 1:
        return 1
    return summer(n-1) + n


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_summer(self):
        n = 10
        sum_expect = 0
        for ii in range(1, n+1):
            sum_expect += ii
        sum_actual = summer(n)
        self.assertEqual(sum_expect, sum_actual)


if __name__ == '__main__':
    unittest.main()
