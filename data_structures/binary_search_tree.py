#!/usr/bin/env python3

import copy

import random
import unittest


class BSTNode:
    def __init__(self, item, parent=None, left=None, right=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, x):
        """
        Returns the node with the item: x
        """
        node_ptr = self._search(x, self.root)
        return node_ptr

    def _search(self, x, node):
        if node is None:
            return None
        if node.item == x:
            return node

        if x < node.item:
            return self._search(x, node.left)
        else:
            return self._search(x, node.right)

    def insert(self, x):
        if self.root is None:
            self.root = BSTNode(x)
        else:
            self._insert(self.root, x, self.root)

    def _insert(self, node, x, parent):
        if node is None:
            node = BSTNode(x, parent=parent, left=None, right=None)
            return

        if x < node.item:
            if node.left is not None:
                self._insert(node.left, x, node)
            else:
                # create node, insert, return
                node.left = BSTNode(x, parent=node, left=None, right=None)
                return
        else:
            if node.right is not None:
                self._insert(node.right, x, node)
            else:
                # create node, insert, return
                node.right = BSTNode(x, parent=node, left=None, right=None)
                return

    def min(self):
        """
        Returns node with the minimum value in the BST
        """
        return self._min(self.root)

    def _min(self, node):
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def max(self):
        """
        Returns node with the maximum value in the BST
        """
        return self._max(self.root)

    def _max(self, node):
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def delete(self, x):
        node_to_delete = self.search(x)
        if node_to_delete is not None:
            # three cases:

            if node_to_delete.left is not None and node_to_delete.right is not None:
                #   node to be deleted has 2 children

                # first, find the minimum element in the right sub-tree
                min_node_right_subtree = self._min(node_to_delete.right)
                # next, replace the node to be deleted with this node

                # NOTE: by simply replacing the item, the pointers are still preserved
                #   we do a deep copy in case item is an object rather than a "simple" datatype
                node_to_delete.item = copy.deepcopy(min_node_right_subtree.item)

                # finally, we need to delete the min_node_right_subtree
                #  it is either a leaf node, or a node with one child
                #  (if it had 2 children, then it wouldn't be the min-node-right-subtree)
                if min_node_right_subtree.left is None and min_node_right_subtree.right is None:
                    # it is a leaf node, just delete the parent's pointers
                    if min_node_right_subtree.parent.left == min_node_right_subtree:
                        min_node_right_subtree.parent.left = None
                    else:
                        min_node_right_subtree.parent.right = None
                else:
                    # there is a child, update the pointers connecting grandparent to grandchild
                    if min_node_right_subtree.left is not None:
                        # child is on left
                        # NOTE: i dont think we need to check the left b/c we are looking at the min-node-right-subtree
                        # if min_node_right_subtree.parent.left == min_node_right_subtree:
                        #     min_node_right_subtree.parent.left = min_node_right_subtree.left
                        # else:
                        #     min_node_right_subtree.parent.right = min_node_right_subtree.left
                        min_node_right_subtree.parent.right = min_node_right_subtree.left
                        # update the grand-child also
                        min_node_right_subtree.left.parent = min_node_right_subtree.parent
                    else:
                        # child is on the right
                        # NOTE: i dont think we need to check the left b/c we are looking at the min-node-right-subtree
                        # if min_node_right_subtree.parent.left == min_node_right_subtree:
                        #     min_node_right_subtree.parent.left = min_node_right_subtree.right
                        # else:
                        #     min_node_right_subtree.parent.right = min_node_right_subtree.right
                        min_node_right_subtree.parent.right = min_node_right_subtree.right
                        # update the grand-child also
                        min_node_right_subtree.right.parent = min_node_right_subtree.parent

            elif node_to_delete.left is None and node_to_delete.right is None:
                if node_to_delete.parent is None:
                    self.root = None
                    return
                #   node to be deleted has no children
                if node_to_delete.parent.left is not None and node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            else:
                #   node to be deleted has 1 child
                if node_to_delete.left is not None:
                    grandchild_node = node_to_delete.left
                else:
                    grandchild_node = node_to_delete.right

                if node_to_delete.parent is None:
                    grandchild_node.parent = None
                    self.root = grandchild_node
                    return

                if node_to_delete.parent.left is not None and node_to_delete.parent.left == node_to_delete:
                    grandchild_node.parent = node_to_delete.parent
                    node_to_delete.parent.left = grandchild_node
                else:
                    grandchild_node.parent = node_to_delete.parent
                    node_to_delete.parent.right = grandchild_node


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def _load_bst(self, num_items=10):
        self.items_to_load = list(range(num_items))
        # randomize the data to get a good tree structure
        random.shuffle(self.items_to_load)

        for item in self.items_to_load:
            self.bst.insert(item)

    def test_insert_search(self):
        num_items_to_insert = 10
        self._load_bst(num_items=num_items_to_insert)
        for item in self.items_to_load:
            n = self.bst.search(item)
            self.assertEqual(item, n.item)
            if n.left is not None:
                self.assertTrue(n.left.item < n.item)
            if n.right is not None:
                self.assertTrue(n.right.item >= n.item)

        # test to ensure that we return none for items that are not in the tree
        items_not_inserted = range(num_items_to_insert+4, num_items_to_insert+8)
        for item in items_not_inserted:
            self.assertEqual(self.bst.search(item), None)

    def test_delete(self):
        num_items_to_insert = 7
        self._load_bst(num_items=num_items_to_insert)
        items_to_delete = self.items_to_load.copy()
        random.shuffle(items_to_delete)

        for item in items_to_delete:
            self.assertEqual(item, self.bst.search(item).item)
            self.bst.delete(item)
            self.assertEqual(None, self.bst.search(item))


if __name__ == '__main__':
    unittest.main()
