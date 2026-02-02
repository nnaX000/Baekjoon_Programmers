import sys
from collections import deque

input=sys.stdin.readline

dequee=deque()

s=input().rstrip()
explode=input().rstrip()

for i in range(len(s)):
    dequee.append(s[i])

    if(dequee):
        if(dequee[-1]==explode[-1]):
            tmp=""
            for j in range(len(explode)):
                if(dequee):
                    tmp+=dequee.pop()

            r_tmp=''.join(reversed(tmp))

            if(r_tmp!=explode):
                for j in r_tmp:
                    dequee.append(j)

print(''.join(dequee) if len(dequee)!=0 else "FRULA")