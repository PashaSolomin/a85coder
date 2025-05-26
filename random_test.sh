#!/bin/bash


dd if=/dev/random bs=2K count=1 status=none of=random.bin


python3 -c 'import sys
import base64
sys.stdout.buffer.write(base64.a85encode(sys.stdin.buffer.read()))'
 <random.bin >random.a85


python3 random_test.py  <random.bin >random.a85.test
cat random.a85.test
#randombin - байтики
#random.a85 - закодированные байтики
#random.bin.test - раскодированные байтики
