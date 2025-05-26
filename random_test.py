#!/usr/bin/env python3
import a85coder
import sys
import base64
data=sys.stdin.buffer.read()
if a85coder.a85e(data)==base64.a85encode(data):
    print("incoder is ok")
else:
    print("incoder is not ok")
encoded=base64.a85encode(data)
#print(encoded)
if a85coder.a85d(encoded)==base64.a85decode(encoded):
    print("decoder is ok")
    #print(a85coder.a85d(encoded))
    #print("\n")
    #print(base64.a85decode(encoded))
else:
    print("decoder is not ok")

