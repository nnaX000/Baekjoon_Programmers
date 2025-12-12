import sys
from collections import Counter

L,R=sys.stdin.readline().rstrip().split(' ')
min_value=float('inf')
count=0

if(len(L)!=len(R)):
    print(0)
    sys.exit(0)

for i in range(len(L)):
    if(L[i]=='8' and R[i]=='8'):
        count+=1
    elif(L[i]!=R[i]):
        break

print(count)