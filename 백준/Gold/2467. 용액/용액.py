import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
#같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만드려고 한다.
A.sort()

left=0
right=len(A)-1

min_value=float('inf')
a=0
b=0

while(left<right):
    tmp=A[left]+A[right]
    if(abs(tmp)<=min_value):
        min_value=abs(tmp)
        a=A[left]
        b=A[right]

    if(tmp<0):
        left+=1
    else:
        right-=1

print(a,b)