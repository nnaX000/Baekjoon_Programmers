import sys

A,B,V=map(int,sys.stdin.readline().rstrip().split(' '))

ram=V-A

day=A-B

if(ram%day==0):
    print((ram//day)+1)
else:
    print((ram//day)+2)