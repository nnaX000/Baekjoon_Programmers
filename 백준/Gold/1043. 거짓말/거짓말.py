import sys
from collections import defaultdict, deque


input=sys.stdin.readline

N,M=map(int,input().split()) # 사람수, 파티 수

person_visit=[False for _ in range(N+1)]
party_visit=[False for _ in range(M+1)]

graph=[set() for _ in range(N+1)]

know=list(map(int,input().split()))
know=know[1:len(know)]

dequee=deque(know)

party=defaultdict(set)

for i in range(M):
    tmp=list(map(int,input().split()))
    for j in range(1,tmp[0]+1):
        party[tmp[j]].add(i+1) # 각 사용자별로 참석하는 파티 아이디 관리
        for l in range(j+1,tmp[0]+1):
            graph[tmp[j]].add(tmp[l])
            graph[tmp[l]].add(tmp[j])

for i in range(len(graph)):
    graph[i]=list(graph[i])

while(dequee):
    person=dequee.popleft()

    for i in party[person]:
        party_visit[i]=True

    for i in range(len(graph[person])):
        if(not person_visit[graph[person][i]]):
            person_visit[graph[person][i]]=True
            dequee.append(graph[person][i])

            for j in party[graph[person][i]]:
                party_visit[j]=True

answer=0

for i in range(len(party_visit)):
    if(not party_visit[i]):
        answer+=1

print(answer-1)