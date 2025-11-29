import sys

M,N=map(int,sys.stdin.readline().rstrip().split(' '))
L=list(map(int,sys.stdin.readline().rstrip().split(' ')))

start=1
end=max(L)
answer=0

while(start<=end):
    middle=(start+end)//2
    tmp=0

    if(middle>0):
        for i in L:
            tmp+=(i//middle)

    if(tmp>=M):
        answer=max(middle,answer)
        start=middle+1
    else:
        end=middle-1

print(answer)