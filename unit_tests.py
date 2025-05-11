#!/usr/bin/env python3
#import a85coder
import base64
def test(a):
    b=a.encode('utf-8')
    encoded=base64.a85encode(b)
    return encoded
def test1(a):
    b=a.encode('utf-8')
    decoded=base64.a85decode(b)
    return decoded
'''class TestASCII85(unittest.TestCase):
    def test_encode1(self):
        encoded=base64.a85encode(b"Blue")
        self.assertEqual(a85e('Blue'), test('Blue'))
    def test_decode1(self):
        self.assertEqual(a85d(';K$2ZEZe=p@<<X'), test(';K$2ZEZe=p@<<X'))
    def test_encode2(self):
        encoded=base64.a85encode(b"Blue")
        self.assertEqual(a85e('Kbpf'), test('Blue'))
    def test_decode2(self):
        self.assertEqual(a85d('DIZ^"DBMG]B-:YnAm5'), test('DIZ^"DBMG]B-:YnAm5'))'''
print(test('Blue\n'))
print(test1('6>UdU$3'))
