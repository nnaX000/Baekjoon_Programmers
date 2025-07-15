import sys

N=int(sys.stdin.readline().strip())

for i in range(N):
    x,y=map(int,sys.stdin.readline().strip().split(' '))

    print(x+y)