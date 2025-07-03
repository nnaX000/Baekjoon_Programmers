import sys
import heapq

jewels=[]
bags=[]

N,K=map(int,sys.stdin.readline().strip().split(' '))

for i in range(N):
    jewels.append(list(map(int,sys.stdin.readline().strip().split(' '))))

for i in range(K):
    bags.append(int(sys.stdin.readline().strip()))

jewels.sort(key=lambda x:x[1],reverse=True)
jewels.sort(key=lambda x:x[0])

bags.sort()
heap=[]
answer=0
j=0

for i in bags:

    while(j<N and i>=jewels[j][0]):
        heapq.heappush(heap,-jewels[j][1])
        j+=1

    if(heap):
        answer+=-heapq.heappop(heap)

print(answer)