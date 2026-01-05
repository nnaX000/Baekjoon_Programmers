import sys

input=sys.stdin.readline

N,M=map(int,input().split())

array=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(i==0):
            if(j!=0):
                array[i][j]=array[i][j-1]+array[i][j]
        else:
            if(j==0):
                array[i][j]=array[i][j]+array[i-1][j]
            else:
                array[i][j]=array[i][j]+array[i-1][j]+array[i][j-1]-array[i-1][j-1]

for i in range(M):
    sum_value=0

    x_1,y_1,x_2,y_2=map(int,input().split())
    x_1-=1
    y_1-=1
    x_2-=1
    y_2-=1

    if(y_1-1<0 and x_1-1>=0):
        print(array[x_2][y_2]-array[x_1-1][y_2])
    elif(y_1-1>=0 and x_1-1<0):
        print(array[x_2][y_2]-array[x_2][y_1-1])
    elif(y_1-1>=0 and x_1-1>=0):
        print(array[x_2][y_2]-array[x_2][y_1-1]-array[x_1-1][y_2]+array[x_1-1][y_1-1])
    else:
        print(array[x_2][y_2])