#!/usr/bin/env python

import unittest


def str_reverse(str_in):
    if len(str_in) == 1:
        return str_in
    elif len(str_in) == 2:
        return str_in[-1] + str_in[0]
    else:
        return str_reverse(str_in[1:]) + str_in[0]


class TestStrReverse(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_str_reverse(self):
        str_in = 'abcde'
        str_out_expected = 'edcba'
        str_out_actual = str_reverse(str_in)
        self.assertEqual(str_out_expected, str_out_actual)


if __name__ == '__main__':
    unittest.main()