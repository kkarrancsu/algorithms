#!/usr/bin/env python3

import doubly_linked_list
import unittest


class Stack:
    """
    Implements a stack using a DoublyLinkedList as the backend
    """
    def __init__(self):
        self.mem = doubly_linked_list.DoublyLinkedList()

    def push(self, x):
        self.mem.insert(x)

    def pop(self):
        x = self.mem.tail.item
        self.mem._delete_last()
        return x


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.num_inserted = 10
        self.items_to_insert = range(self.num_inserted)
        for i in self.items_to_insert:
            self.stack.push(i)

    def test_pop(self):
        pop_expected = list(self.items_to_insert)
        pop_expected.reverse()
        for pop_val in pop_expected:
            pop_actual = self.stack.pop()
            self.assertEqual(pop_val, pop_actual)

    def test_insert_pop(self):
        pop_expected = list(self.items_to_insert)
        pop_expected.reverse()
        pop_expected = pop_expected[0:4]
        for pop_val in pop_expected:
            pop_actual = self.stack.pop()
            self.assertEqual(pop_val, pop_actual)

        # now insert and pop n times as another test
        push_pop_vals = [10, 20, 30, 40, 50]
        for push_pop_val in push_pop_vals:
            self.stack.push(push_pop_val)
            pop_actual = self.stack.pop()
            self.assertEqual(pop_actual, push_pop_val)


if __name__ == '__main__':
    unittest.main()
