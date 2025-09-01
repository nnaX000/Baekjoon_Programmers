import sys
from collections import deque

sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())
dequee=deque()

train=[[] for i in range(N+1)]

for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    train[x].append(y)
    train[y].append(x)

circle=set()

check=False

max_len=0

#순환선 찾아내기
def circle_dfs(visited):
    global max_len
    global circle
    global check

    for i in range(len(train[visited[-1]])):

        if(len(visited)>=3 and train[visited[-1]][i]==origin_node):
            circle=set(visited[:])
            check=True
            return

        elif(train[visited[-1]][i] not in visited):
            visited.append(train[visited[-1]][i])
            circle_dfs(visited)
            visited.pop()

for i in range(1,N+1):
    visited=[i]
    origin_node=i
    circle_dfs(visited)
    if(check):
        break

dist=[-1 for i in range(N+1)]
dequee=deque()

for i in circle:
    dist[i]=0
    dequee.append(i)

#간선으로부터 순환선까지의 거리 찾아내기
while(dequee):
    tmp=dequee.popleft()
    for k in train[tmp]:
        if dist[k]==-1 :
            dist[k]=dist[tmp]+1
            dequee.append(k)

print(*dist[1:])

#놓친부분
#1. 굳이 dfs해서 순환경로 찾을때 가장 크게 커버하는 범위 찾겠다고 끝까지 다 할 필요없고 그냥 하나 찾으면 그걸로 break
#2. 일일히 bfs해서 간선 최소 거리 찾는게 아니라 한번만 돌려서 찾는 방법 있었음