import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
dequee=deque()
answer=[]

for i in range(1,N+1):
    dequee.append(i)

while(dequee):
    tmp=dequee.popleft()
    answer.append(tmp)
    
    if(dequee):
        move=dequee.popleft()
        dequee.append(move)

print(*answer)