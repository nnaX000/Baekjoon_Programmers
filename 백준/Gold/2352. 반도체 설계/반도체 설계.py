import sys
import bisect

n=int(sys.stdin.readline().rstrip())
port=list(map(int,sys.stdin.readline().rstrip().split(' ')))
L=[port[0]]

for i in range(1,n):
    tmp = port[i]

    if(tmp<=L[-1]):
        pos=bisect.bisect_left(L,tmp)
        L[pos]=tmp
    else:
        L.append(tmp)

print(len(L))