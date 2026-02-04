import sys

input=sys.stdin.readline

N,M=map(int,input().split())

candi=list(map(int,input().split()))
candi.sort()

def dfs(arr,visited):
    if(len(arr)==M):
        print(*arr)
        return
    
    visit=set()
    for i in range(len(candi)):
        if(candi[i] not in visit and not visited[i]):
            visited[i]=True
            arr.append(candi[i])
            visit.add(candi[i])
            dfs(arr,visited)
            arr.pop()
            visited[i]=False

visited=[False for _ in range(N)]
dfs([],visited)