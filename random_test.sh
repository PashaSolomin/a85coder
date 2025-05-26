#!/bin/bash


dd if=/dev/random bs=2K count=1 status=none of=random.bin


python3 -c 'import sys
import base64
sys.stdout.buffer.write(base64.a85encode(sys.stdin.buffer.read()))'
 <random.bin >random.a85


python3 a85coder.py  <random.bin >random.a85.test
python3 a85coder.py -d  <random.a85 >random.bin.test
#echo "random.bin.test (decoded)"
#cat random.bin.test
#echo "random.bin (original)"
#cat random.bin

if ! cmp -s random.a85 random.a85.test; then
echo "Encoder failed on random data" >&2
exit 1
fi


if ! cmp -s random.bin random.bin.test; then
echo "Decoder failed on random data" >&2
exit 1
fi


echo Ok! >&2
exit 0

#randombin - байтики
#random.a85 - закодированные байтики
#random.bin.test - раскодированные байтики
