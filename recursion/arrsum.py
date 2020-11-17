#!/usr/bin/env python

import unittest
import random


def arrsum(x_in):
    if len(x_in) == 1:
        return x_in[0]
    return arrsum(x_in[1:]) + x_in[0]


class TestMySum(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_arrsum(self):
        n = 10
        x_in = []
        for ii in range(n):
            z = random.randint(0, 100)
            x_in.append(z)
        sum_expect = sum(x_in)
        sum_actual = arrsum(x_in)
        self.assertEqual(sum_expect, sum_actual)


if __name__ == '__main__':
    unittest.main()
