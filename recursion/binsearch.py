#!/usr/bin/env python

import unittest
import random


def binsearch(x, target):
    """
    Searches an sorted input list, x, for a target
    """
    # basecase
    if len(x) == 1:
        if x[0] == target:
            return True
        else:
            return False

    mid = int(len(x)/2)
    if target == x[mid]:
        return True
    elif target > x[mid]:
        return binsearch(x[mid+1:], target)
    else:
        return binsearch(x[0:mid], target)


class TestBinSearch(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_binsearch(self):
        n = 10
        x = list(range(n))
        for ii in range(n):
            self.assertTrue(binsearch(x, ii))
        self.assertFalse(binsearch(x, 11))


if __name__ == '__main__':
    unittest.main()