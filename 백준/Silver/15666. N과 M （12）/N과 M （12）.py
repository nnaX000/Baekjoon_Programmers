import sys

input=sys.stdin.readline

N,M=map(int,input().split())

candi=list(map(int,input().split()))
candi.sort()

def dfs(start,arr):
    if(len(arr)==M):
        print(*arr)
        return
    
    visited=set()
    for i in range(start,len(candi)):
        if(candi[i] not in visited):
            visited.add(candi[i])
            arr.append(candi[i])
            dfs(i,arr)
            arr.pop()

dfs(0,[])