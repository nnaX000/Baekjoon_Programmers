import sys
from itertools import combinations
from collections import defaultdict,deque

input=sys.stdin.readline

N=int(input())
half=N//2
people=list(map(int,input().split()))
people_sv=sum(people)

graph=[[] for _ in range(N+1)]
candi=[i+1 for i in range(N)]

adjust=defaultdict(set)
answer=float('inf')

for i in range(1,N+1):
    tmp=list(map(int,input().split()))

    for j in range(1,len(tmp)):
        graph[i].append(tmp[j])
        graph[tmp[j]].append(i)

def bfs(n):
    global visited
    global result
    global ours

    dq=deque()
    dq.append(n)

    while(dq):
        k=dq.popleft()

        for i in range(len(graph[k])):
            if(not visited[graph[k][i]] and graph[k][i] in ours):
                visited[graph[k][i]]=True
                dq.append(graph[k][i])
                result.add(graph[k][i])


for i in range(1,half+1):
    for j in combinations(candi,i):
        first_1=j[0]
        team_1=set(j)
        check_1=False

        team_2=[]
        check_2=False

        for k in range(1,N+1):
            if(k not in team_1):
                team_2.append(k)

        first_2=team_2[0]
        team_2=set(team_2)

        ours=team_1
        result=set()
        result.add(first_1)
        visited=[False for _ in range(N+1)]
        bfs(first_1)

        if(len(result & team_1)!=len(team_1)):
            check_1=True

        if(not check_1):
            ours=team_2
            result=set()
            result.add(first_2)
            visited=[False for _ in range(N+1)]
            bfs(first_2)

            if(len(result & team_2)!=len(team_2)):
                check_2=True

            if(not check_2):
                sv_1=0
                sv_2=0

                for k in team_1:
                    sv_1+=people[k-1]

                sv_2=people_sv-sv_1

                answer=min(answer,abs(sv_1-sv_2))

print(answer if answer!=float('inf') else -1)