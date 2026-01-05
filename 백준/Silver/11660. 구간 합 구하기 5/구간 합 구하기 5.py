import sys

input=sys.stdin.readline

N,M=map(int,input().split())

array=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1,N):
        array[i][j]=array[i][j-1]+array[i][j]

for i in range(M):
    sum_value=0

    x_1,y_1,x_2,y_2=map(int,input().split())
    x_1-=1
    y_1-=1
    x_2-=1
    y_2-=1

    for j in range(x_1,x_2+1):
        if(y_1!=0):
            sum_value+=(array[j][y_2]-array[j][y_1-1])
        else:
            sum_value+=array[j][y_2]

    print(sum_value)