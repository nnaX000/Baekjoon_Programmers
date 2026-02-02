import sys

input=sys.stdin.readline

N,M=map(int,input().split())

array=[i+1 for i in range(N)]

def dfs(start,arr):
    if(len(arr)==M):
        print(*arr)
        return
    
    for i in range(start,len(array)):
        arr.append(array[i])
        dfs(i,arr)
        arr.pop()

dfs(0,[])