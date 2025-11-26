import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
A.sort()

min_value=float('inf')

candi=[0,0,0]

for i in range(N):
    one=A[i]

    start=0
    end=N-1

    while(start<end):
        sum_value=one+A[start]+A[end]

        if(abs(sum_value)<min_value and i!=start and i!=end):
            min_value=abs(sum_value)
            candi[0]=i
            candi[1]=start
            candi[2]=end

        if(sum_value<0):
            start+=1
        else:
            end-=1

for i in range(3):
    candi[i]=A[candi[i]]

candi.sort()

print(*candi)