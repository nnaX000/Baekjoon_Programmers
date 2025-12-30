import sys
import heapq

input=sys.stdin.readline

N=int(input())

heap=[]
heapq.heapify(heap)

for i in range(N):
    x=int(input())

    if(x!=0):
        if(x<0):
            tmp=-x
        else:
            tmp=x

        heapq.heappush(heap,(tmp,x))
    else:
        if(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)