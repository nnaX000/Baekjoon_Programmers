import sys
from collections import deque

A,B,C=map(int,sys.stdin.readline().rstrip().split(' '))

combination=[[0,1],[1,2],[0,2]]
dequee=deque()
dequee.append([A,B,C])
visited=set()
visited.add((A,B,C))

while(dequee):
    tmp=dequee.popleft()
    a=tmp[0]
    b=tmp[1]
    c=tmp[2]

    if(a==b==c):
        print(1)
        sys.exit(0)
    
    for i in range(3):
        target_1=combination[i][0]
        target_2=combination[i][1]

        na=a
        nb=b
        nc=c

        if(tmp[target_1]!=tmp[target_2]):
            if(tmp[target_1]>tmp[target_2]):
                bigger=target_1
                smaller=target_2
            else:
                bigger=target_2
                smaller=target_1

            n_bigger=tmp[bigger]-tmp[smaller]
            n_smaller=tmp[smaller]+tmp[smaller]

            if(bigger==0):
                na=n_bigger
            elif(bigger==1):
                nb=n_bigger
            else:
                nc=n_bigger

            if(smaller==0):
                na=n_smaller
            elif(smaller==1):
                nb=n_smaller
            else:
                nc=n_smaller

            if((na,nb,nc) not in visited):
                dequee.append([na,nb,nc])
                visited.add((na,nb,nc))

print(0)