#!/usr/bin/env python

import unittest
import random


class MinHeap:
    def __init__(self, heap_size):
        self.n = heap_size
        self.heap_backend = [None] * self.n
        self.cur_max_idx = -1

    def insert(self, x):
        self.cur_max_idx += 1
        if self.cur_max_idx >= self.n:
            raise ValueError("Heap full!")
        self.heap_backend[self.cur_max_idx] = x

        self._bubble_up(self.cur_max_idx)

    @staticmethod
    def _get_parent_idx(ii):
        if ii == 0:
            return None
        else:
            return int(ii / 2)

    @staticmethod
    def _get_young_child_idx(ii):
        # This returns the *left* child.  The +1 is there b/c we are index-0 based.
        return int(2*ii + 1)

    def _bubble_up(self, insert_idx):
        parent_ii = MinHeap._get_parent_idx(insert_idx)
        if parent_ii is None:
            return
        else:
            if self.heap_backend[parent_ii] > self.heap_backend[insert_idx]:
                # swap
                tmp_val = self.heap_backend[insert_idx]
                self.heap_backend[insert_idx] = self.heap_backend[parent_ii]
                self.heap_backend[parent_ii] = tmp_val
                # continue bubbling if necessary
                self._bubble_up(parent_ii)

    def get_min(self):
        return self.heap_backend[0]

    def pop_min(self):
        min_val = self.heap_backend[0]
        self.heap_backend[0] = self.heap_backend[self.cur_max_idx]
        self.cur_max_idx -= 1
        # restore the heap
        self._bubble_down(0)

        return min_val

    def _bubble_down(self, p):
        c = MinHeap._get_young_child_idx(p)
        min_index = p

        # find the index of the minimum value
        for ii in range(2):
            # check the left and right child of the young-child
            if (c + ii) <= self.cur_max_idx:
                # if those values are lower than the current min-index, reset the min-index
                if self.heap_backend[min_index] > self.heap_backend[c+ii]:
                    min_index = c+ii

        if min_index != p:
            # swap p and min-index
            tmp = self.heap_backend[min_index]
            self.heap_backend[min_index] = self.heap_backend[p]
            self.heap_backend[p] = tmp
            # continue bubbling down
            self._bubble_down(min_index)


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap(10)

    def _load_heap(self, num_items=10):
        self.items_to_load = list(range(num_items))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

        for item in self.items_to_load:
            self.heap.insert(item)

    def test_min_pop(self):
        num_items = 10
        self._load_heap(num_items=num_items)
        for ii in range(num_items):
            min_popped = self.heap.pop_min()
            self.assertEqual(min_popped, ii)


if __name__ == '__main__':
    unittest.main()