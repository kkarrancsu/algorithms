#!/usr/bin/env python


import unittest
import random


def insertion_sort(x):
    for ii in range(1, len(x)):
        jj = ii
        while (jj-1 >= 0) and (x[jj] < x[jj-1]):
            tmp = x[jj]
            x[jj] = x[jj-1]
            x[jj-1] = tmp
            jj -= 1

    return x


class TestInsertionSort(unittest.TestCase):
    def setUp(self) -> None:
        self.items_to_load = list(range(10))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

    def test_sort(self):
        sort_expected = self.items_to_load.copy()
        sort_expected.sort()
        sort_actual = insertion_sort(self.items_to_load)
        self.assertEqual(sort_expected, sort_actual)


if __name__ == '__main__':
    unittest.main()