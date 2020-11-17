#!/usr/bin/env python

import unittest


def _test_palindrome(str_in, ii_lo, ii_hi):
    """
    Check if a string is a palindrome, recursively.  We note the following observation:
    Examples:
        odd length string: madam
        step-0: d
        step-1: a-d-a
        step-2: m-ada-m

        even length string: aabbaa
        step-0: bb
        step-1: a-bb-a
        step-2: a-abba-a

    So, the base cases are if the string length is 1 or 2.  otherwise, start from
    the middle of the string and work your way out and test strings of length 2.
    """
    if ii_lo >= 0 and ii_hi < len(str_in):
        # keep checking as long as we are in bounds of the string
        if str_in[ii_lo] == str_in[ii_hi]:
            return _test_palindrome(str_in, ii_lo - 1, ii_hi + 1)
        else:
            return False
    # if we got here, that means that we've checked all the letters and the
    return True


def test_palindrome(str_in):
    mid = int(len(str_in)/2)
    if len(str_in) % 2 == 0:
        return _test_palindrome(str_in, mid-1, mid)
    else:
        return _test_palindrome(str_in, mid-1, mid+1)


class TestPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_a(self):
        z = test_palindrome('madam')
        print('z', z)
        z = test_palindrome('adam')
        print('z', z)
        z = test_palindrome('hello')
        print('z', z)


if __name__ == '__main__':
    unittest.main()