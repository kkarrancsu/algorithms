#!/usr/bin/env python

import unittest
import random


def selection_sort(x, min_func=None):
    if min_func is None:
        min_func = min
    sorted_x = [None]*len(x)
    ii = 0
    len_x = len(x)
    while ii < len_x:
        min_val = min_func(x)
        sorted_x[ii] = min_val
        ii += 1
        x.remove(min_val)

    return sorted_x


class TestSelectionSort(unittest.TestCase):
    def setUp(self) -> None:
        self.items_to_load = list(range(10))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

    def test_sort(self):
        sort_expected = self.items_to_load.copy()
        sort_expected.sort()
        sort_actual = selection_sort(self.items_to_load)
        self.assertEqual(sort_expected, sort_actual)


if __name__ == '__main__':
    unittest.main()
