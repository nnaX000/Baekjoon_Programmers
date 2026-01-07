import sys
from collections import deque

input=sys.stdin.readline

S=input().rstrip()
explode=input().rstrip()

dequee=deque()

for i in S:
    dequee.append(i)
    if(dequee[-1]==explode[-1]):
        tmp=""
        length=len(dequee)
        for j in range(min(len(explode),length)):
            tmp+=dequee.pop()

        tmp=''.join(list(reversed(tmp)))

        if(tmp!=explode):
            for j in tmp:
                dequee.append(j)

if(len(dequee)==0):
    print("FRULA")
else:
    print(''.join(dequee))