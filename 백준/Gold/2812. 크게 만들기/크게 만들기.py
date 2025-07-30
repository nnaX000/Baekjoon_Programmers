import sys
from collections import deque

N,K=map(int,sys.stdin.readline().rstrip().split(' '))
tmp=sys.stdin.readline().rstrip()

dequee=deque()
erase_num=0

for idx,i in enumerate(tmp):
    while(dequee and erase_num<K):
        if(dequee[-1]<i):
            erase_num+=1
            dequee.pop()
        else:
            break
    dequee.append(i)

if(erase_num<K):
    dequee=list(dequee)
    dequee=dequee[:N-K]

print(''.join(dequee))