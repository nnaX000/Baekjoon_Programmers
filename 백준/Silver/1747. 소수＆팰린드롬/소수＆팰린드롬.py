import sys
from collections import deque

answer=0
array=[0]*1100001#0소수 1소수아님
array[0]=1
array[1]=1
num=int(sys.stdin.readline())
string_num=str(num)
stop=False

for i in range(2,550001):
    for j in range(i+i,1100001,i):
        array[j]=1

for i in range(num,1100001):
    dequee=deque()
    if(array[i]==0):
        for j in str(i):
            dequee.append(j)
            
        if(len(dequee)==1):
            answer=i
            break

        while(len(dequee)>1):
            a=dequee.pop()
            b=dequee.popleft()
            if(a!=b):
                break
            if(len(dequee)==1 or len(dequee)==0):
                stop=True
                break
    if(stop):
        answer=i
        break

print(answer)