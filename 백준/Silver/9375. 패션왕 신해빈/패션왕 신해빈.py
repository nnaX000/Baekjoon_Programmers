import sys
from collections import defaultdict

input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())
    answer=1
    closet=defaultdict(int)

    kinds=set()

    for j in range(n):
        cloth,kind=input().split()
        kinds.add(kind)
        closet[kind]+=1

    for key,values in closet.items():
        answer*=(values+1)

    print(answer-1)