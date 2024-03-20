import sys
from collections import deque
dequee=deque()
computerNum=int(sys.stdin.readline())
caseNum=int(sys.stdin.readline())
array=[[] for i in range(computerNum+1)]
dequee.append(1)
visited=set()
for i in range(caseNum):
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    array[tmp[0]].append(tmp[1])
    array[tmp[1]].append(tmp[0])
while(dequee):
    target=dequee.pop()
    if (target not in visited):
        visited.add(target)
        dequee.extend(array[target])
print(len(visited)-1)