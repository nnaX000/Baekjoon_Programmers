import sys

a1, a0 = map(int,sys.stdin.readline().rstrip().split(' '))
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

ram_1=((a1*n0)+a0)-(c*n0)
ram_2=((a1*(n0+1))+a0)-(c*(n0+1))

if(ram_1<=0 and ram_2<=ram_1):
    print(1)
else:
    print(0)