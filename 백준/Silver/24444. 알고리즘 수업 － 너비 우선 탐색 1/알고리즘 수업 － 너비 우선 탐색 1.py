import sys
from collections import deque
dequee=deque()
node,line,start=map(int,sys.stdin.readline().split(' '))
array=[[] for i in range(node+1)]
dequee.append(start)
answer=[0 for i in range(node)]
visited=set()
index=1
for i in range(line):
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    array[tmp[0]].append(tmp[1])
    array[tmp[1]].append(tmp[0])
while(dequee):
    target=dequee.popleft()
    if(target not in visited):
        visited.add(target)
        answer[target-1]=index
        index+=1
        dequee.extend(sorted(array[target]))
for i in answer:
    print(i)