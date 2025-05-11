#!/usr/bin/env python3
import a85coder
import sys
import base64
#code = base64.a85decode if sys.argv[1] == '-d' else base64.a85encode
def test(a, t):
    if t==1:
        b=a.encode('utf-8')
        res=base64.a85encode(b)
    if t==2:
        b=a.encode('utf-8')
        res=base64.a85decode(b)
    return res

class TestASCII85(unittest.TestCase):
    def test_encode1(self):
        encoded=base64.a85encode(b"Blue")
        self.assertEqual(a85e('Blue'), test('Blue', 1))
    def test_decode1(self):
        self.assertEqual(a85d(';K$2ZEZe=p@<<X'), test(';K$2ZEZe=p@<<X', 2))
    def test_encode2(self):
        encoded=base64.a85encode(b"Blue")
        self.assertEqual(a85e('Kbpf'), test('Blue', 1))
    def test_decode2(self):
        self.assertEqual(a85d('DIZ^"DBMG]B-:YnAm5'), test('DIZ^"DBMG]B-:YnAm5', 2))
