#!/usr/bin/env python

import unittest


def mypow(a, b):
    """
    Computes a^b

    a^b = product(a,i=0 ...b-1)
    """
    if b == 1:
        return a
    return mypow(a, b-1)*a


class TestPow(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_pow(self):
        a = 4
        b = 2
        z = mypow(a, b)
        self.assertEqual(pow(a,b), z)


if __name__ == '__main__':
    unittest.main()