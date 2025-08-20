import sys
from collections import deque

N,M=map(int,sys.stdin.readline().rstrip().split(' ')) # 사람 수, 친구 관계 수

dequee=deque()
arr=[]
friend=[[] for i in range(N)]
check=False

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))
    friend[a].append(b)
    friend[b].append(a)

def dfs(num,visited,k):
    global check 

    if(num==5):
        print(1)
        check=True
        sys.exit(0)

    for i in friend[k]:
        if(not visited[i]):
         visited[i]=True
         num+=1
         dfs(num,visited,i)
         num-=1
         visited[i]=False

visited=[False for i in range(N)]

for i in range(N):
   visited[i]=True
   dfs(1,visited,i)
   visited[i]=False

if(not check):
   print(0)