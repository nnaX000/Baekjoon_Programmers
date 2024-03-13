import heapq
import sys
num=int(sys.stdin.readline())
answer=[]
list=[]
length=0
for i in range(num):
    tmp=-int(sys.stdin.readline())
    if(tmp==0):
        if(length==0):
            answer.append(0)
        else:
            a=heapq.heappop(list)
            answer.append(-a)
            length-=1
    else:
        heapq.heappush(list,tmp)
        length+=1
for i in answer:
    print(i)