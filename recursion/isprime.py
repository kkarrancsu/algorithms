#!/usr/bin/env python

import unittest


def _isprime(n, k):
    if k == 2:
        if n % 2 == 0:
            return False
        else:
            return True

    if n % k == 0:
        return False
    else:
        return _isprime(n, k-1)


def isprime(n):
    """
    Checks if n is prime.
    checking if a # is prime is equivalent to checking if n is divisible by any number
    below n, > 1
    """
    return _isprime(n, n-1)


class TestIsPrime(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_isprime(self):
        self.assertTrue(isprime(3))
        self.assertTrue(isprime(5))
        self.assertFalse(isprime(6))


if __name__ == "__main__":
    unittest.main()