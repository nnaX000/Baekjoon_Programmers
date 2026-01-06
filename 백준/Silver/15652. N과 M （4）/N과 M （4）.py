import sys

input=sys.stdin.readline

N,M=map(int,input().split())
array=[i for i in range(1,N+1)]

def dfs(num,start):
    if(len(num)==M):
        print(*num)
        return
    
    for i in range(start,len(array)):
        num.append(array[i])
        dfs(num,i)
        num.pop()

dfs([],0)