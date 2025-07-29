import sys
import heapq
from collections import deque

N=int(sys.stdin.readline().rstrip())

classes=[]

for i in range(N):
    classes.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

classes.sort(key=lambda x:x[0])
classes=deque(classes)

heap=[]
tmp=classes.popleft()
heapq.heappush(heap,tmp[1])

while(classes):
    tmp=classes.popleft()
    start=tmp[0]
    end=tmp[1]

    tmp=heapq.heappop(heap)

    if(tmp>start):
        heapq.heappush(heap,tmp)
        heapq.heappush(heap,end)
    else:
        heapq.heappush(heap,end)

print(len(heap))