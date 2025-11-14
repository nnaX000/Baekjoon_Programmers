import sys

N=int(sys.stdin.readline().rstrip())
k=int(sys.stdin.readline().rstrip())

start,end = 0,N*N

while(start<=end):
    middle = (start+end)//2

    count=0
    for i in range(1,N+1):
        count+=min(middle//i,N)

    if(count>=k):
        answer=middle
        end=middle-1
    else:
        start=middle+1

print(answer)