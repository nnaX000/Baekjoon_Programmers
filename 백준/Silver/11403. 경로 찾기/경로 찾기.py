import sys

N=int(sys.stdin.readline().rstrip())
array=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(N)]

for i in range(N):
    for j in range(N):
        for l in range(N):
            if(array[j][i]==1 and array[i][l]==1):
                array[j][l]=1

for i in array:
    print(*i)