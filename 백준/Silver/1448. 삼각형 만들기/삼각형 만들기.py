import sys
from itertools import combinations

input=sys.stdin.readline

N=int(input())
s=[]
answer=float('-inf')

for i in range(N):
    s.append(int(input()))

s.sort(reverse=True)

for i in range(N-2):
    first=s[i]
    second=s[i+1]
    third=s[i+2]

    if(first<second+third):
        answer=first+second+third
        break

print(answer if answer!=float('-inf') else -1)