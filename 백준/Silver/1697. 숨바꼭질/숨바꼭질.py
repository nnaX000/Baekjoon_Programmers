import sys
from collections import deque
dequee=deque()
subin,brother=map(int,sys.stdin.readline().split(' '))
def BFS(subin,brother):
    visited=set()
    dequee = deque()
    dequee.append(subin)
    count = 0
    visited.add(subin)
    while(dequee):
        count+=1
        size=len(dequee)
        for i in range(size):
            tmp=dequee.popleft()
            if(tmp==brother):
                return count
            else:
                for j in [tmp+1,tmp-1,tmp*2]:
                    if((j>=0 and j<=100000) and j not in visited):
                        visited.add(j)
                        dequee.append(j)
answer=BFS(subin,brother)
print(answer-1)