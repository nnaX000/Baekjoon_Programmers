import sys

A,B,C=map(int,sys.stdin.readline().rstrip().split(' '))

tmp=A^B
tmp_2=tmp^B

if(C%2==1):
    print(tmp)
else:
    print(tmp_2)