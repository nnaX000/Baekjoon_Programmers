import sys

input=sys.stdin.readline

T=int(input())

count=[[0,0] for i in range(41)]

count[0][0]=1
count[1][1]=1

arr=[]

for i in range(T):
    N=int(input())
    arr.append(N)

for i in range(2,max(arr)+1):
    count[i][0]=count[i-1][0]+count[i-2][0]
    count[i][1]=count[i-1][1]+count[i-2][1]

for i in arr:
    print(count[i][0],count[i][1])