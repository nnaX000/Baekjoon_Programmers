import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

T=int(input())

def dfs(x):
    global answer
    visited[x]=True
    nxt=students[x]

    if(not visited[nxt]):
        dfs(nxt)
    else: # 방문함
        if(not finished[nxt]): # 근데 finished 처리가 안돼있으면 이번 턴 path에 있다는거
            cur=nxt
            tmp=1
            while(cur!=x):
                cur=students[cur]
                tmp+=1
            answer+=tmp

    finished[x]=True

for i in range(T):
    n=int(input())
    answer=0

    students=[0]+list(map(int,input().split()))

    visited=[False for _ in range(n+1)]
    finished=[False for _ in range(n+1)]

    for j in range(1,n+1):
        if(not visited[j]):
            dfs(j)

    print(n-answer)