import sys
from collections import deque
import itertools

N=int(sys.stdin.readline())
SCV=list(map(int,sys.stdin.readline().rstrip().split(' ')))
power=[9,3,1]
visited=set()
visited.add(tuple(SCV))

dequee=deque()
dequee.append([SCV,0])

while(dequee):
    tmp,value=dequee.popleft()
    candi=list(itertools.permutations(tmp,N))

    for i in candi:
        new=[]
        for jdx,j in enumerate(i):
            new_value=i[jdx]-power[jdx]
            if(new_value<0):
                new_value=0
            new.append(new_value)
        if(tuple(new) not in visited):
            dequee.append([new,value+1])
            visited.add(tuple(new))

        if(sum(new)==0):
            print(value+1)
            sys.exit(0)