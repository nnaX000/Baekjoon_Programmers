import sys

input=sys.stdin.readline

N,M=map(int,input().split())
array=list(map(int,input().split()))
array.sort()

answer=[]

def dfs(visited):
    if(len(answer)==M):
        print(*answer)
        return
    
    used=set()
    for i in range(N):
        if(array[i] not in used and not visited[i]):
            used.add(array[i])
            visited[i]=True
            answer.append(array[i])
            dfs(visited)
            answer.pop()
            visited[i]=False

visited=[False for _ in range(N)]
dfs(visited)