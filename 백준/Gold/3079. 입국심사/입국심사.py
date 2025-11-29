import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
T=[]

for i in range(N):
    T.append(int(sys.stdin.readline().rstrip()))

start=1
end=10**20
answer=0

while(start<=end):
    middle=(start+end)//2
    tmp=0

    for i in T:
        tmp+=(middle//i)

    if(tmp>=M):
        answer=middle
        end=middle-1
    else:
        start=middle+1

print(answer)