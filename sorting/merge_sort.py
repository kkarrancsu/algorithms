#!/usr/bin/env python

import unittest
import random

from data_structures.my_queue import Queue


def merge(x, lo, mid, hi):
    q1 = Queue()
    q2 = Queue()

    for ii in range(lo, mid+1):
        q1.enqueue(x[ii])
    for ii in range(mid+1, hi+1):
        q2.enqueue(x[ii])

    ii = lo
    while q1.n > 0 or q2.n > 0:
        q1_val = q1.get_queue_top()
        q2_val = q2.get_queue_top()
        if q1_val is not None and q2_val is not None:
            if q1_val <= q2_val:
                x[ii] = q1.dequeue()
            else:
                x[ii] = q2.dequeue()
            ii += 1
        else:
            break

    while q1.n > 0:
        x[ii] = q1.dequeue()
        ii += 1

    while q2.n > 0:
        x[ii] = q2.dequeue()
        ii += 1


def merge_sort(x, lo, hi):
    if lo < hi:
        mid = int((lo+hi)/2)
        merge_sort(x, lo, mid)
        merge_sort(x, mid+1, hi)
        merge(x, lo, mid, hi)


class TestMergeSort(unittest.TestCase):
    def setUp(self) -> None:
        self.num_items_to_sort = 8
        self.items_to_load = list(range(self.num_items_to_sort))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

    def test_sort(self):
        sort_expected = self.items_to_load.copy()
        sort_expected.sort()
        merge_sort(self.items_to_load, 0, self.num_items_to_sort-1)  # it is an in-place sort
        self.assertEqual(sort_expected, self.items_to_load)


if __name__ == '__main__':
    unittest.main()
