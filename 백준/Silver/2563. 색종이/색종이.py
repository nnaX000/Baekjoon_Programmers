import sys

N=int(sys.stdin.readline().strip())

axis=[[0 for i in range(101)]for j in range(101)]

answer=0

for i in range(N):
    count=0
    x,y=map(int,sys.stdin.readline().strip().split(' '))

    for j in range(x,x+10):
        for k in range(y,y+10):
            if(axis[k][j]==1):
                count+=1
            else:
               axis[k][j]=1

    answer+=(100-count)

print(answer)
