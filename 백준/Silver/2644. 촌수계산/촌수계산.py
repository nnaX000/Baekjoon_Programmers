import sys
import heapq

input=sys.stdin.readline

n=int(input()) # 전체 사람 수

p1,p2=map(int,input().split())

m=int(input())

family=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())

    family[a].append(b)
    family[b].append(a)

hq=[]
heapq.heapify(hq)
heapq.heappush(hq,(0,p1))

answer=[float('inf') for _ in range(n+1)]

while(hq):
    cost,pos=heapq.heappop(hq)

    if(cost>answer[pos]):
        continue

    if(pos==p1):
        answer[pos]=0

    for i in range(len(family[pos])):
        if(answer[family[pos][i]]>answer[pos]+1):
            answer[family[pos][i]]=answer[pos]+1
            heapq.heappush(hq,(answer[pos]+1,family[pos][i]))

print(answer[p2] if answer[p2]!=float('inf') else -1)