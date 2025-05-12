#!/usr/bin/env python3
import a85coder
import sys
import base64
import unittest
def test(a, t):
    if t==1:
        res=base64.a85encode(a)
    if t==2:
        res=base64.a85decode(a)
    return res

class TestASCII85(unittest.TestCase):
    def test_encode1(self):
        self.assertEqual(a85coder.a85e(b'Blue'), test(b'Blue', 1))
    def test_decode1(self):
        self.assertEqual(a85coder.a85d(b';K$2ZEZe=p@<<X'), test(b';K$2ZEZe=p@<<X', 2))
    def test_encode2(self):
        self.assertEqual(a85coder.a85e(b'Kbpf'), test(b'Kbpf', 1))
    def test_decode2(self):
        self.assertEqual(a85coder.a85d(b'DIZ^"DBMG]B-:YnAm5'), test(b'DIZ^"DBMG]B-:YnAm5', 2))
if __name__ == '__main__':
    unittest.main()
