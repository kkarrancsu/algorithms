#!/usr/bin/env python

import unittest
import random
import copy


def _swap(x, a, b):
    tmp = x[a]
    x[a] = x[b]
    x[b] = tmp


def _partition(x_in, l, h):
    p = h          # in this implementation, the pivot is always the last element
    firsthigh = l  # variable reprsents the "frontier" above which all elements are greater, and below which all
                   # elements are smaller than the chosen pivot point

    for ii in range(l, h+1):
        if x_in[ii] < x_in[p]:
            _swap(x_in, ii, firsthigh)  # firsthigh is the location of the frontier
            firsthigh += 1              # advance the frontier
    _swap(x_in, p, firsthigh)

    return firsthigh


def _quicksort(x_in, l, h):
    if h-l > 0:
        p = _partition(x_in, l, h)
        _quicksort(x_in, l, p-1)
        _quicksort(x_in, p+1, h)


def quicksort(x_in):
    # an in-place sort
    _quicksort(x_in, 0, len(x_in)-1)


class TestSelectionSort(unittest.TestCase):
    def setUp(self) -> None:
        self.items_to_load = list(range(10))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

    def test_sort(self):
        sort_expected = self.items_to_load.copy()
        sort_expected.sort()
        sort_actual = copy.copy(self.items_to_load)
        quicksort(sort_actual)
        self.assertEqual(sort_expected, sort_actual)


if __name__ == '__main__':
    unittest.main()
