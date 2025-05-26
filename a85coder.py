#!/usr/bin/env python3
import sys
def a85e(a):
    #print('a', a)
    count=0
    p=[i for i in a]
    #print(p)
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
           raise ValueError('Недопустимый символ в ASCII85')
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
            #print(j, encoded[i][j]*85**(4-j))
            num+=encoded[i][j]*85**(4-j)
        if num>2**32-1:
            #print('num', num)
            #print(b)
            raise ValueError('Ascii85 overflow')
        encoded[i]=hex(num)[2:]
    #print('3', encoded)
    if encoded!=[]:
        if len(encoded[-1])<8:
            encoded[-1]='0'*(8-len(encoded[-1]))+encoded[-1]
    else:
        return b''
    #print('4', encoded)
    for i in range(len(encoded)):
        b1 = hex((int(encoded[i], 16) >> 24) & 0xFF)
        b2 = hex((int(encoded[i], 16) >> 16) & 0xFF)
        b3 = hex((int(encoded[i], 16) >> 8) & 0xFF)
        b4 = hex(int(encoded[i], 16) & 0xFF)
        B=[b1, b2, b3, b4]
        #print(B)
        for i in range(len(B)):
            if len(B[i])==3:
                B[i]=B[i][:2]+'0'+B[i][2:]
            Bytes.append(B[i])
    #print('5', Bytes)
    while count>0:
        Bytes.pop(-1)
        count-=1
    #print('6', Bytes)
    #print(len(Bytes))
    p = [int(Bytes[i],16) for i in range(len(Bytes))]
    #print(p)
    for i in range(len(p)):
        decoded+=bytes([p[i]])
    #print(decoded)
    return decoded

#if sys.argv[1] == '-e':
#    code = a85e
#elif sys.argv[1] == '-d':
#    code = a85d
code = a85d if sys.argv[1] == '-d' else a85e
#sys.stdout.buffer.write(code(sys.stdin.buffer.read()))
print(code(sys.stdin.buffer.read()))
#print(a85d(b'%&gMH<s'))
#print(a85e(b'\xca\x8b;\x0eW'))
