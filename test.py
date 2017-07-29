#!/usr/bin/env python
#test
import os
import unittest

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        assert rv.data == b'Hello World'


if __name__ == '__main__':
    unittest.main()
