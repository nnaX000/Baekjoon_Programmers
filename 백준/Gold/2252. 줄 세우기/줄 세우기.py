import sys
from collections import deque, defaultdict

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
info=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(M)]
visited=[False for i in range(N+1)]
answer=[]

forward_dic=defaultdict(list)
backward_dic=defaultdict(int) #진입차수

dequee=deque()

for a,b in info:
    forward_dic[a].append(b)
    backward_dic[b]+=1

for i in range(1,N+1):
    if(i not in backward_dic and not visited[i]):
        dequee.append(i)
        visited[i]=True

while(len(answer)<N):

    tmp=dequee.popleft()
    answer.append(tmp)

    for i in forward_dic[tmp]:
        backward_dic[i]-=1
        if(backward_dic[i]==0 and not visited[i]):
            dequee.append(i)
            visited[i]=True

print(*answer)