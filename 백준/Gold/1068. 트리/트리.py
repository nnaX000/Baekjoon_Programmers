import sys
from collections import defaultdict,deque

input=sys.stdin.readline

N=int(input())
node=list(map(int,input().split()))
remove=int(input())
root=0
roots=defaultdict(list)
answer=[[float('inf'),float('inf')] for _ in range(51)]
visited=[False for _ in range(N+1)]
result=0

for i in range(N):
    if(node[i]==-1):
        root=i
    else:
        roots[node[i]].append(i)

if(remove!=root):
    answer[root]=[-1,-1]

dq=deque()
dq.append(root)

while(dq):
    tmp=dq.popleft()

    if(tmp==remove):
        continue

    for value in roots[tmp]:
        if(not visited[value] and value!=remove):
            visited[value]=True
            answer[value]=[-1,-1]
            if(answer[tmp][0]==-1):
                answer[tmp][0]=value
            else:
                answer[tmp][1]=value

            dq.append(value)

for i in range(51):
    if(answer[i][0]==-1 and answer[i][1]==-1):
        result+=1

print(result)