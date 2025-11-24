import sys
import bisect

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
L=[]
L.append(A[0])

for i in range(1,len(A)):
    if(L[-1]<A[i]):
        L.append(A[i])
    else:
        tmp=bisect.bisect_left(L,A[i])
        L[tmp]=A[i]

print(len(L))