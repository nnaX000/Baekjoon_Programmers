import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

#부모 노드, 자식 노드, 가중치

n=int(input())
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    tmp=input()

    p,j,w=map(int,tmp.split())
    graph[p].append([j,w])
    graph[j].append([p,w])

def dfs(n,cost):
    global answer

    for i in range(len(graph[n])):
        if(not visited[graph[n][i][0]]):
            visited[graph[n][i][0]]=True
            answer[graph[n][i][0]]=cost+graph[n][i][1]
            dfs(graph[n][i][0],answer[graph[n][i][0]])

visited=[False for _ in range(n+1)]
answer=[0 for _ in range(n+1)]
visited[1]=True
dfs(1,0)

max_value=max(answer)
for i in range(1,n+1):
    if(max_value==answer[i]):
        dot=i

answer=[0 for _ in range(n+1)]
visited=[False for _ in range(n+1)]
visited[dot]=True
dfs(dot,0)

print(max(answer))