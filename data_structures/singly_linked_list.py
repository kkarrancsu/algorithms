#!/usr/bin/env python3

import unittest

class SinglyLinkedListNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        if self.head is None:
            return None
        else:
            cur_ptr = self.head
            while cur_ptr is not None and cur_ptr.item != item:
                cur_ptr = cur_ptr.next
            if cur_ptr is None:
                return None
            else:
                if cur_ptr.item == item:
                    return cur_ptr
                else:
                    return None

    def insert(self, item):
        new_node = SinglyLinkedListNode(item)
        if self.head is None:
            self.head = new_node
        else:
            cur_ptr = self.head
            while cur_ptr.next is not None:
                cur_ptr = cur_ptr.next
            cur_ptr.next = new_node

    def delete(self, item):
        if self.head is not None:
            # special case if we are deleting head
            if self.head.item == item:
                self.head = self.head.next
                return

            cur_ptr = self.head
            while cur_ptr.next is not None and cur_ptr.next.item != item:
                cur_ptr = cur_ptr.next
            if cur_ptr.next is None:
                return
            if cur_ptr.next.item == item:
                # we didn't find the item to be deleted
                if cur_ptr.next.next == None:
                    # we are deleting the tail
                    cur_ptr.next = None
                else:
                    cur_ptr.next = cur_ptr.next.next

    def _delete_head(self):
        """
        convenience method implemented for Queue implementation
        """
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SinglyLinkedList()
        self.num_inserted = 10
        self.items_to_insert = range(self.num_inserted)
        for i in self.items_to_insert:
            self.ll.insert(i)

    def test_insert(self):
        # traverse through the list and ensure elements are inserted in the
        # order we specified
        cur_ptr = self.ll.head
        ii = 0
        while cur_ptr is not None:
            self.assertEqual(cur_ptr.item, self.items_to_insert[ii])
            ii += 1
            cur_ptr = cur_ptr.next
        assert ii == self.num_inserted

    def test_search(self):
        for search_item in self.items_to_insert:
            node = self.ll.search(search_item)
            self.assertEqual(node.item, search_item)

        num_extra = 4
        not_inserted_search_list = range(self.num_inserted, self.num_inserted+num_extra)
        for search_item in not_inserted_search_list:
            node = self.ll.search(search_item)
            self.assertIsNone(node)

    def test_delete(self):
        delete_items = self.items_to_insert
        for d in delete_items:
            before_delete_ptr = self.ll.search(d)
            self.assertEqual(before_delete_ptr.item, d)
            self.ll.delete(d)
            after_delete_ptr = self.ll.search(d)
            self.assertIsNone(after_delete_ptr)

    def test_delete_reverse_order(self):
        delete_items = list(self.items_to_insert)
        delete_items.reverse()
        for d in delete_items:
            before_delete_ptr = self.ll.search(d)
            self.assertEqual(before_delete_ptr.item, d)
            self.ll.delete(d)
            after_delete_ptr = self.ll.search(d)
            self.assertIsNone(after_delete_ptr)

    def test_delete_shuffle_order(self):
        delete_items = list(self.items_to_insert)
        shift_amt = 4
        b = delete_items[shift_amt:] + delete_items[:shift_amt]
        for d in delete_items:
            before_delete_ptr = self.ll.search(d)
            self.assertEqual(before_delete_ptr.item, d)
            self.ll.delete(d)
            after_delete_ptr = self.ll.search(d)
            self.assertIsNone(after_delete_ptr)


if __name__ == '__main__':
    unittest.main()
