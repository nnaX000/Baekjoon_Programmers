from collections import deque
import sys

dequee=deque()

N=int(input())
answer=[]

for i in range(N):
    temp=input()

    if(" " in temp):
        command, num=temp.split(' ')
    else:
        command=temp

    if(command=="push_front"):
        dequee.appendleft(int(num))
    
    if(command=="push_back"):
        dequee.append(int(num))
    
    if(command=="pop_front"):
        if(dequee):
            tmp=dequee.popleft()
            answer.append(tmp)
        else:
            answer.append(-1)

    if(command=="pop_back"):
        if(dequee):
            tmp=dequee.pop()
            answer.append(tmp)
        else:
            answer.append(-1)
    
    if(command=="size"):
        answer.append(len(dequee))

    if(command=="empty"):
        if(dequee):
            answer.append(0)
        else:
            answer.append(1)

    if(command=="front"):
        if(dequee):
            answer.append(dequee[0])
        else:
            answer.append(-1)

    if(command=="back"):
        if(dequee):
            answer.append(dequee[-1])
        else:
            answer.append(-1)

for i in answer:
    print(i)
