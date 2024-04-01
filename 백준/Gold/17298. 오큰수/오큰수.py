#거꾸로 가면서
from collections import deque
size=int(input())
dequee=deque()
num=deque()
array=list(map(int,input().split(' ')))
stand=0
count=0
num.append(0)
dequee.append(array[0])
answer=[-1 for i in range((size))]
for i in range(1,len(array)):
    count = 0
    if(array[i]<=dequee[-1]):
        dequee.append(array[i])
        num.append(i)
    else:
        while(len(dequee)>0 and dequee[-1]<array[i]):
            dequee.pop()
            a=num.pop()
            count+=1
            answer[a]=array[i]
        dequee.append(array[i])
        num.append(i)
for i in answer:
    print(i,end=" ")
