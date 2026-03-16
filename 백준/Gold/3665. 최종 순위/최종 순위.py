import sys
from collections import deque

input=sys.stdin.readline

T=int(input())

result=[]

# 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표

for i in range(T):

    n=int(input())
    t=list(map(int,input().split())) # 작년 등수
    m=int(input())
    answer=[]
    visited=[False for _ in range(n+1)]

    if(m==0):
        result.append(t)
    else:
        switch=set()

        prev=[set() for _ in range(n+1)]
        cnt=[0 for _ in range(n+1)]

        unique=True
        possible=True

        dq=deque()

        for j in range(len(t)):
            for l in range(j+1,len(t)):
                prev[t[j]].add(t[l])
                cnt[t[l]]+=1

        for j in range(m):
            a,b=map(int,input().split())
            if(a in prev[b]):
                prev[b].remove(a)
                cnt[a]-=1
                prev[a].add(b)
                cnt[b]+=1
            else:
                prev[a].remove(b)
                cnt[b]-=1
                prev[b].add(a)
                cnt[a]+=1

        for j in range(1,n+1):
            prev[j]=list(prev[j])

        for j in range(1,n+1):
            if(cnt[j]==0):
                dq.append(j)

        if(len(dq)>1):
            unique=False

        while(dq):
            x=dq.popleft()
            visited[x]=True
            answer.append(x)

            num=0
            for j in range(len(prev[x])):
                if(not visited[prev[x][j]]):
                    cnt[prev[x][j]]-=1

                    if(cnt[prev[x][j]]==0):
                        num+=1
                        dq.append(prev[x][j])

            if(num>1):
                unique=False

        for j in range(1,n+1):
            if(not visited[j]):
                possible=False
                break
        
        if(not possible):
            result.append("I")
        elif(not unique):
            result.append("?")
        else:
            result.append(answer)

for i in result:
    if(i=="I"):
        print("IMPOSSIBLE")
    else:   
        print(*i)