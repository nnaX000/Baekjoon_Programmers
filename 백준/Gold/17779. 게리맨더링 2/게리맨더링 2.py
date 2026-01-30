import sys

input=sys.stdin.readline

N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]

# [0,0] [0,1]
# [1,0] [1,1]

dx=[1,1,-1,-1]
dy=[-1,1,1,-1]

answer=float('inf')

def calcul(x,y,d1,d2):
    result=[0,0,0,0,0]
    assign=[[0 for _ in range(N)] for _ in range(N)]

    #border line
    for i in range(4):
        if(i==0):
            for j in range(d1):
                x+=dx[i]
                y+=dy[i]

                if(0<=x<N and 0<=y<N):
                    assign[x][y]=5
                else:
                    return -1
        elif(i==1):
            for j in range(d2):
                x+=dx[i]
                y+=dy[i]

                if(0<=x<N and 0<=y<N):
                    assign[x][y]=5
                else:
                    return -1
        elif(i==2):
            for j in range(d1):
                x+=dx[i]
                y+=dy[i]

                if(0<=x<N and 0<=y<N):
                    assign[x][y]=5
                else:
                    return -1
        else:
            for j in range(d2):
                x+=dx[i]
                y+=dy[i]

                if(0<=x<N and 0<=y<N):
                    assign[x][y]=5
                else:
                    return -1

    last_y=0     
    for i in range(N):
        if(assign[x+d1+d2][i]==5):
            last_y=i
            break

    # 가운데에 5 채우기
    for i in range(N):
        check=False

        if(i!=x and i!=x+d1+d2):
            for j in range(N):
                if(assign[i][j]==5 and not check):
                    check=True
                elif(assign[i][j]==0 and check):
                    assign[i][j]=5
                elif(assign[i][j]==5 and check):
                    break
    
    # 가장자리 숫자 채우기
    for i in range(N):
        if(i<x):
            for j in range(y+1):
                assign[i][j]=1
            
            for j in range(y+1,N):
                assign[i][j]=2
        elif(i>=x and i<=x+d1+d2):
            left=0
            right=0

            if(i<=x-1+d1):
                left=1
            else:
                left=3

            if(i<=x+d2): #3
                right=2
            else:
                right=4

            check=False

            for j in range(N):
                if(assign[i][j]==0 and not check):
                    assign[i][j]=left
                elif(assign[i][j]==5):
                    check=True
                elif(assign[i][j]==0 and check):
                    assign[i][j]=right
        else:
            for j in range(last_y):
                assign[i][j]=3

            for j in range(last_y,N):
                assign[i][j]=4

    #print(x,y,d1,d2)
    #print(assign)

    #result에 더하기
    for i in range(N):
        for j in range(N):
            result[assign[i][j]-1]+=array[i][j]

    return max(result)-min(result)

for i in range(N):
    for j in range(N):

        for k in range(1,N):
            for l in range(1,N):
                result = calcul(i,j,k,l)

                if(result!=-1):
                    answer=min(answer,result)

print(answer)