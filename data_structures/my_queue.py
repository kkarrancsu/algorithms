#!/usr/bin/env python3

import data_structures.singly_linked_list as singly_linked_list
import unittest


class Queue:
    """
    Queue implementation with a SinglyLinkedList as the backend
    """
    def __init__(self):
        self.mem = singly_linked_list.SinglyLinkedList()
        self.n = 0

    def enqueue(self, x):
        self.mem.insert(x)
        self.n += 1

    def dequeue(self):
        x = self.mem.head.item
        self.mem._delete_head()
        self.n -= 1
        return x

    def get_queue_top(self):
        if self.n > 0:
            return self.mem.head.item
        else:
            return None


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.num_inserted = 10
        self.items_to_insert = range(self.num_inserted)
        for i in self.items_to_insert:
            self.queue.enqueue(i)

    def test_dequeue(self):
        dequeue_list = list(self.items_to_insert)
        for dq in dequeue_list:
            dq_item_actual = self.queue.dequeue()
            self.assertEqual(dq, dq_item_actual)


if __name__ == '__main__':
    unittest.main()
