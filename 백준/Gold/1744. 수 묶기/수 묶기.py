import sys
from collections import deque

N=int(input())

array=[]

for i in range(N):
    array.append(int(sys.stdin.readline().strip()))

array.sort()

dequee=deque(array)

answer=0

while(dequee and dequee[-1]>=1): # 양수쪽
    if(len(dequee)>=2):
        a=dequee.pop()
        b=dequee.pop()

        if(a>=1 and b>=1):
            answer+=max(a*b,a+b)
        elif(a>=1 and b<1):
            answer+=a
            dequee.append(b)
            break
    else:
        a=dequee.pop()
        
        answer+=a

while(dequee): # 음수쪽
    if(len(dequee)>=2):
        a=dequee.popleft()
        b=dequee.popleft()

        answer+=a*b
    else:
        a=dequee.popleft()

        answer+=a

print(answer)