import sys
from collections import Counter

input=sys.stdin.readline

N,M=map(int,input().split())
lamp=[input().rstrip() for _ in range(N)]
n_lamp=Counter(lamp)
K=int(input())
answer=float('-inf')


for key,value in n_lamp.items():
    zeros=key.count('0')
    if(K>=zeros and (K-zeros)%2==0):
        answer=max(answer,value)

print(answer if answer!=float('-inf') else 0)