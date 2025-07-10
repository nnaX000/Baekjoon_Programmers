import sys
import heapq

N=int(sys.stdin.readline().strip())

q=[]
room=[]

for i in range(N):
    start,end=map(int,sys.stdin.readline().strip().split(' '))
    heapq.heappush(q,[start,end])

while(q):
    occupy=False
    tmp=heapq.heappop(q)
    if(room and room[0]<=tmp[0]): # 힙은 제일 작은 것부터 반환하므로 제일 빠른 종료시간보다 시작시간이 빠르면 더이상 볼 것도 없음
        heapq.heappop(room)

    heapq.heappush(room, tmp[1])

print(len(room))