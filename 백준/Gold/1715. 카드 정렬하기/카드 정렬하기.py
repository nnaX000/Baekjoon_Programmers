import sys
import heapq

answer=0

array=[]

N=int(sys.stdin.readline())

for i in range(N):
    array.append(int(sys.stdin.readline()))

heapq.heapify(array)

if(len(array)>=2):
    while(array):
        one=heapq.heappop(array)
        second=heapq.heappop(array)

        sum_value=one+second

        answer+=sum_value

        if(len(array)>0):
            heapq.heappush(array,sum_value)
else:
    answer=0

print(answer)