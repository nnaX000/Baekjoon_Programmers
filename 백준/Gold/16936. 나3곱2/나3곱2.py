import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
B=list(map(int,sys.stdin.readline().rstrip().split(' ')))

for i in range(N):
    ram=B[:]

    ram.remove(B[i])
    path=[B[i]]
    visited=set((1,B[i])) # 순서, 숫자
    
    dequee=deque()
    dequee.append((ram,path))

    while(dequee):
        ram, path = dequee.popleft()
        tmp=path[-1]

        if(len(ram)==0):
            print(*path)
            sys.exit(0)

        if(tmp%3==0 and tmp//3 in ram and (len(path)+1, tmp//3) not in visited):
            visited.add((len(path)+1, tmp//3))
            ram.remove(tmp//3)
            path.append(tmp//3)
            nram=ram[:]
            npath=path[:]
            dequee.append((nram,npath))
            ram.append(tmp//3)
            path.pop()

        if(tmp*2 in ram and (len(path)+1, tmp*2) not in visited):
            visited.add((len(path)+1, tmp*2))
            ram.remove(tmp*2)
            path.append(tmp*2)
            nram=ram[:]
            npath=path[:]
            dequee.append((nram,npath))
            ram.append(tmp*2)
            path.pop()