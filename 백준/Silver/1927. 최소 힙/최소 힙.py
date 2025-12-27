import sys
import heapq

input=sys.stdin.readline

heap=[]
heapq.heapify(heap)

N=int(input())

for i in range(N):
    tmp=int(input())

    if(tmp==0):
        if(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,tmp)