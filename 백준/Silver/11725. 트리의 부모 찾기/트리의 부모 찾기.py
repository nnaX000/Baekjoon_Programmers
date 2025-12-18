import sys
from collections import defaultdict,deque

tree=defaultdict(list)
N=int(sys.stdin.readline().rstrip())
answer=[0 for i in range(N+1)]
tree[1]=[]

candi=defaultdict(list)
dequee=deque()
dequee.append(1)

for i in range(N-1):
    a,b=(map(int,sys.stdin.readline().rstrip().split(' ')))
    candi[a].append(b)
    candi[b].append(a)

visited=set()

while(dequee):
    tmp=dequee.popleft()

    for i in candi[tmp]:
        if(i not in visited):
            answer[i]=tmp
            visited.add(i)
            dequee.append(i)

for i in range(2,len(answer)):
    print(answer[i])