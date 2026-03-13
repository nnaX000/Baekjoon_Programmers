import sys

input=sys.stdin.readline

T=int(input())
answer=[]

for i in range(T):
    N,M=map(int,input().split())
    for j in range(M):
        a,b=map(int,input().split())
    answer.append(N-1)

for i in answer:
    print(i)