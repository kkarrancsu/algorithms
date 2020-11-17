#!/usr/bin/env python

import unittest
import random


def mymin(x_in):
    # base case
    if len(x_in) == 2:
        if x_in[0] < x_in[1]:
            return x_in[0]
        else:
            return x_in[1]

    return min(mymin(x_in[1:]), x_in[0])


class TestMyMin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_mymin(self):
        n = 10
        x_in = []
        for ii in range(n):
            z = random.randint(0, 100)
            x_in.append(z)
        min_expect = min(x_in)
        min_actual = mymin(x_in)
        self.assertEqual(min_expect, min_actual)


if __name__ == '__main__':
    unittest.main()