import sys

N=int(sys.stdin.readline().rstrip())
relation_N=int(sys.stdin.readline().rstrip())

relation=[[] for i in range(N+1)]
answer=0

for i in range(relation_N):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))
    relation[a].append(b)
    relation[b].append(a)

visited=set()

def dfs(virus):
    global answer

    for i in range(len(relation[virus])):
        if(relation[virus][i] not in visited):
            visited.add(relation[virus][i])
            dfs(relation[virus][i])

visited.add(1)
dfs(1)

print(len(visited)-1)