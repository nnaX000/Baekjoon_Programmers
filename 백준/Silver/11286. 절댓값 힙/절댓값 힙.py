import heapq
import sys
num=int(sys.stdin.readline())
array=[]
answer=[]
realNum=[]
for i in range(num):
    tmp=int(sys.stdin.readline())
    if(tmp==0):
        if(len(array)==0):
            answer.append(0)
        else:
           a=heapq.heappop(array)
           answer.append(a[1])
    else:
        heapq.heappush(array,(abs(tmp),tmp))
for i in answer:
    print(i)