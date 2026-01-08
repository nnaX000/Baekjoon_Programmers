import sys

input=sys.stdin.readline

N=int(input())

dp_max=[[0,0] for _ in range(3)] #최대, 최소

max_value=float('-inf')
min_value=float('inf')

for i in range(N):
    array=list(map(int,input().split()))

    if(i==0):
        for j in range(3):
            dp_max[j][0]=array[j]
            dp_max[j][1]=array[j]
    else:
        one_max,one_min = dp_max[0][0], dp_max[0][1]
        two_max,two_min = dp_max[1][0], dp_max[1][1]
        th_max,th_min = dp_max[2][0], dp_max[2][1]

        dp_max[0][0]=max(one_max,two_max)+array[0]
        dp_max[1][0]=max(one_max,two_max,th_max)+array[1]
        dp_max[2][0]=max(two_max,th_max)+array[2]

        dp_max[0][1]=min(one_min,two_min)+array[0]
        dp_max[1][1]=min(one_min,two_min,th_min)+array[1]
        dp_max[2][1]=min(two_min,th_min)+array[2]

for i in range(3):
    max_value=max(max_value,dp_max[i][0])
    min_value=min(min_value,dp_max[i][1])

print(max_value,min_value)