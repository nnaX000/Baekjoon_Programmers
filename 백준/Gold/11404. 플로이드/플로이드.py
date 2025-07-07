import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

distance=[[float('inf') for j in range(n+1)] for i in range(n+1)]

for i in range(n+1):
    distance[i][i]=0

for i in range(m):
    start,end,cost=map(int,sys.stdin.readline().strip().split(' '))
    distance[start][end]=min(cost,distance[start][end])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if(distance[i][j]==float('inf')):
            distance[i][j]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        print(distance[i][j],end=" ")

    print()