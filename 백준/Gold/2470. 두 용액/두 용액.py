import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split(' ')))

A.sort()

answer=[0,0]
min_dist=float('inf')

start=0 # 인덱스 기준
end=N-1 # 인덱스 기준

while(start<end):
    if(abs(A[start]+A[end])<min_dist):
        min_dist=abs(A[start]+A[end])
        answer[0]=A[start]
        answer[1]=A[end]

    if(A[start]+A[end]<0):
        start+=1
    else:
        end-=1

print(*answer)