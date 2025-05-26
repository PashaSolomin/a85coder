#!/usr/bin/env python3
import sys
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
        print(i,b[i], chr(b[i]), byt)
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
            print(j, encoded[i][j]*85**(4-j))
            num+=encoded[i][j]*85**(4-j)
        print('num', num)
        encoded[i]=hex(num)[2:]
    #print('3', encoded)
    if encoded!=[]:
        if len(encoded[-1])<8:
            encoded[-1]='0'*(8-len(encoded[-1]))+encoded[-1]
    else:
        return b''
    #print('4', encoded)
    for i in range(len(encoded)):
        for j in range(0, len(encoded[i]), 2):
            Bytes.append(f'0x{encoded[i][j:j+2]}')
    #print('5', Bytes)
    while count>0:
        Bytes.pop(-1)
        count-=1
    #print('6', Bytes)
    #print(len(Bytes))
    for i in range(len(Bytes)):
        print('Bytes[i]', Bytes[i])
        print('int(Bytes[i], 16)', int(Bytes[i], 16))
        char=chr(int(Bytes[i], 16))
        print('char', char)
        b=char.encode('utf-8')
        print('b', b)
        decoded+=b
        print(decoded)
    #print('7', decoded)
    return decoded 
#code = a85d if sys.argv[1] == '-d' else a85e
sys.stdout.buffer.write(a85d(sys.stdin.buffer.read()))
