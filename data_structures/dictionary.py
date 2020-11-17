#!/usr/bin/env python3

import math
import unittest


class Dictionary:
    """
    Dictionary implementation with an unsorted list as the backend.
    Each element in the list is a tuple.  The first element in the tuple
    is the hash-code. The second element is a list of tuples, stored as (k,v)
    pairs.
    """
    def __init__(self, mem_size=1000):
        self.mem_size = mem_size
        self.mem = [-1]*mem_size
        self.keys = []  # makes it easy to search whether key already exists

    def _hash(self, k):
        k_str = str(k)
        # the max value of ord() is documented here:
        #  https://docs.python.org/3/library/functions.html#chr
        alpha = 0x10FFFF
        S = len(k)
        sum = 0
        for ii, ch in enumerate(k_str):
            exp_arg = S-(ii+1)
            sum += (math.pow(alpha, exp_arg)*ord(ch))
        return sum

    def _get_index(self, k):
        hash_sum = self._hash(k)
        index = int(hash_sum % self.mem_size)
        return hash_sum, index

    def search(self, k):
        if k in self.keys:
            _, ii = self._get_index(k)
            if len(self.mem[ii]) == 2:  # need this check in order to ensure that an element has been inserted here
                kv_pairs = self.mem[ii][1]  # ii=0 is the hash-code, ii=1 is the list of k/v pair tuples
                for kv_pair in kv_pairs:
                    if kv_pair[0] == k:
                        return kv_pair[1]
        return None

    def insert(self, k, v):
        hash_code, ii = self._get_index(k)
        if isinstance(self.mem[ii], tuple) and len(self.mem[ii]) == 2:
            kv_pairs = self.mem[ii][1]
            ii_to_delete = None
            for jj, kv_pair in enumerate(kv_pairs):
                if k == kv_pair[0]:
                    ii_to_delete = jj
                    break
            if ii_to_delete is not None:
                # delete old k/v pair
                self.mem[ii][1].pop(ii_to_delete)
                # insert new k/v pair at end of list
                self.mem[ii][1].append((k, v))
            else:
                # otherwise, append to the list
                self.mem[ii][1].append((k, v))
        else:
            # create a new list
            self.mem[ii] = (hash_code, [(k, v)])
        self.keys.append(k)

    def delete(self, k):
        if k in self.keys:
            _, ii = self._get_index(k)
            if len(self.mem[ii]) == 2:  # need this check in order to ensure that an element has been inserted here
                kv_pairs = self.mem[ii][1]  # ii=0 is the hash-code, ii=1 is the list of k/v pair tuples
                ii_to_delete = None
                for jj, kv_pair in enumerate(kv_pairs):
                    if kv_pair[0] == k:
                        ii_to_delete = jj
                        break
                if ii_to_delete is not None:
                    self.mem[ii][1].pop(ii_to_delete)
                    self.keys.remove(k)


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dict = Dictionary()
        self.num_inserted = 10
        self.items_inserted = range(self.num_inserted)
        self.keys_inserted = []
        for v in self.items_inserted:
            k = chr(v)
            self.dict.insert(k, v)
            self.keys_inserted.append(k)

    def test_insert_search(self):
        for k, v in zip(self.keys_inserted, self.items_inserted):
            self.assertTrue(k in self.dict.keys)
            # now retrieve the element associated w/ that key, ensure it is what we expect
            self.assertEqual(v, self.dict.search(k))

    def test_insert_update_search(self):
        # here, we test whether updating the value for an existing key works properly
        keys_to_update = self.keys_inserted[3:7]
        updated_values = [x-15 for x in self.items_inserted[3:7]]
        for k, v in zip(keys_to_update, updated_values):
            self.dict.insert(k, v)
            self.assertEqual(v, self.dict.search(k))

    def test_delete(self):
        delete_keys = self.keys_inserted[3:7]
        for dk in delete_keys:
            self.dict.delete(dk)
            self.assertTrue(dk not in self.dict.keys)
            self.assertEqual(self.dict.search(dk), None)

if __name__ == '__main__':
    unittest.main()
