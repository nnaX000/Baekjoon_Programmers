import sys
from collections import defaultdict

input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())
    closet=defaultdict(int)

    for j in range(n):
        tmp,kind=input().split()
        closet[kind]+=1

    result=1
    for key,value in closet.items():
        result*=(value+1)

    print(result-1)