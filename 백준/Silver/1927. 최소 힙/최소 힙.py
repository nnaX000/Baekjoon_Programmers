import heapq
import sys
num=int(sys.stdin.readline())
array=[]
answer=[]
for i in range(num):
    tmp=int(sys.stdin.readline())
    if(tmp==0):
        if(len(array)==0):
            answer.append(0)
        else:
            a=heapq.heappop(array)
            answer.append(a)
    else:
        heapq.heappush(array,tmp)

for i in answer:
    print(i)
