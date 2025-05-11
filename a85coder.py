#!/usr/bin/env python3
import sys
def a85e(a):
    count=0
    Bytes=[hex(i) for i in a]
    Bytes4=[]
    encoded=b''
    for i in range(len(Bytes)):
        if len(Bytes[i])==3:
            Bytes[i]=f'0x0{Bytes[i][-1]}'
    #print(Bytes)
    while len(Bytes)%4!=0:
        Bytes.append('0x00')
        count+=1
    #print(Bytes)
    for i in range(0, len(Bytes), 4):
        Bytes4.append(Bytes[i:i+4])
    #print(Bytes4)
    for i in range(len(Bytes4)):
        num32='0x'
        for j in Bytes4[i]:
            num32+=j[2:]
        Bytes4[i]=num32
    #print(Bytes4)
    for i in range(len(Bytes4)):
        Bytes4[i]=int(Bytes4[i], 16)
    #print('nums',  Bytes4)
    for i in range(len(Bytes4)):
        digits=[]
        for j in range(4, -1, -1):
            digits.append((Bytes4[i]//85**j)%85)
        Bytes4[i]=digits
    #print(Bytes4)
    for i in range(len(Bytes4)):
        for j in range(len(Bytes4[i])):
            s=f'{chr(Bytes4[i][j]+33)}'
            encoded+=s.encode()
    #print(encoded)
    if count>0:
        encoded=encoded[:-count]
    #print(encoded)
    return encoded
def a85d(b):
    a=b''
    encoded=[]
    Bytes=[]
    decoded=b''
    count=0
    #print(b)
    #print(len(b))
    for i in range(len(b)):
        byt=f'{chr(b[i])}'.encode()
        #print(i,b[i], chr(b[i]), byt)
        if not  byt.isspace():
           a+=byt
        elif not byt.isspace() and (a[i]<33 or a[i]>117):
           print("Недопустимый символ для ASCII85", file=sys.stderr)
           sys.exit(1)
    #print('a', a)
    while len(a)%5!=0:
        a+=b'u'
        count+=1
    for i in range(0, len(a), 5):
        encoded.append(a[i:i+5])
    #print('1', encoded)
    for i in range(len(encoded)):
        digits=[]
        for j in range(len(encoded[i])):
            #print(encoded[i][j])
            digits.append(encoded[i][j]-33)
        encoded[i]=digits
    #print('2', encoded)
    for i in range(len(encoded)):
        num=0
        for j in range(len(encoded[i])):
            num+=encoded[i][j]*85**(4-j)
        encoded[i]=hex(num)[2:]
    #print('3', encoded)
    if len(encoded[-1])<8:
        encoded[-1]='0'*(8-len(encoded[-1]))+encoded[-1]
    #print('4', encoded)
    for i in range(len(encoded)):
        for j in range(0, len(encoded[i]), 2):
            Bytes.append(f'0x{encoded[i][j:j+2]}')
    #print('5', Bytes)
    while count>0:
        Bytes.pop(-1)
        count-=1
    #print('6', Bytes)
    for i in range(len(Bytes)):
        char=chr(int(Bytes[i], 16))
        b=char.encode()
        decoded+=b
    #print('7', decoded)
    return decoded
code = a85d if sys.argv[1] == '-d' else a85e
sys.stdout.buffer.write(code(sys.stdin.buffer.read()))
