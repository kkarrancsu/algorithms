#!/usr/bin/env python

"""
Heap sort implementation, which is effectively a selection sort with a min-heap datastructure
rather than a list
"""

import unittest
import random

from data_structures.min_heap import MinHeap


def heap_sort(x: MinHeap):
    """
    Sorts data in x
    :param x: a MinHeap datastructure w/ data to be sorted
    :return:
    """
    x_sorted = [None]*x.n
    for ii in range(x.n):
        min_val = x.pop_min()
        x_sorted[ii] = min_val

    return x_sorted


class TestHeapSort(unittest.TestCase):
    def setUp(self) -> None:
        num_items_to_sort = 10
        self.items_to_load = list(range(num_items_to_sort))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

        # put the items into a heap, b/c our HeapSort API requires items to be sorted
        # to be in the MinHeap Datastructure
        self.heap = MinHeap(num_items_to_sort)
        for item in self.items_to_load:
            self.heap.insert(item)

    def test_sort(self):
        sort_expected = self.items_to_load.copy()
        sort_expected.sort()
        sort_actual = heap_sort(self.heap)
        self.assertEqual(sort_expected, sort_actual)


if __name__ == '__main__':
    unittest.main()