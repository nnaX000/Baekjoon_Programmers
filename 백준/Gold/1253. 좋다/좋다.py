import sys
from collections import defaultdict

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
A.sort()
result=0

for i in range(N):
    target=A[i]
    left,right=0,N-1

    while(left<right):
        sum_value=A[left]+A[right]

        if(sum_value==target):
            if(left!=i and right!=i):
                result+=1
                break
            elif(left==i):
                left+=1
            else:
                right-=1

        elif(sum_value>target):
            right-=1
        else:
            left+=1

print(result)