import sys
from collections import defaultdict

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

address=defaultdict(str)

for i in range(N):
    a,b=sys.stdin.readline().rstrip().split(' ')
    address[a]=b

for i in range(M):
    a=sys.stdin.readline().rstrip()
    print(address[a])