import sys
import heapq

N=int(sys.stdin.readline().rstrip())
conference=[]

heap=[]

heapq.heapify(heap)

for i in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    conference.append(tmp)

conference.sort(key=lambda x:x[0])

for start,end in conference:
    if(not heap):
        heapq.heappush(heap,end)
    else:
        end_time=heapq.heappop(heap)

        if(end_time<=start):
            heapq.heappush(heap,end)
        else:
            heapq.heappush(heap,end_time)
            heapq.heappush(heap,end)

print(len(heap))