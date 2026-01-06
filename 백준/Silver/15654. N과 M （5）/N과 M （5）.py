import sys
from itertools import permutations

input=sys.stdin.readline

N,M=map(int,input().split())

array=list(map(int,input().split()))
array.sort()

for i in permutations(array,M):
    print(*i)