#!/usr/bin/env python

import unittest

import rosunit

PKG = "rostest_example"


class TestError(unittest.TestCase):

    # This should be a @classmethod but isn't so there is an error
    def setUpClass(cls):
        pass

    def test_obvious(self):
        self.assertEqual(1, 1, "this never fails")


if __name__ == "__main__":
    rosunit.unitrun(PKG, "error_triggered", TestError)
