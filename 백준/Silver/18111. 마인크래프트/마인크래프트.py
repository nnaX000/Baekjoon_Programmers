import sys

input=sys.stdin.readline

N,M,B=map(int,input().split())
land=[list(map(int,input().split())) for _ in range(N)]

#블록을 제거하는게 더 큰 cost -> 차라리 쌓는게 나음.
#땅 높이는 256블록 초과 X
#심을수있는 블록수 정해져있음

min_value=min([min(i) for i in land])
max_value=max([max(i) for i in land])

if(max_value>256):
    max_value=256

if(min_value<0):
    min_value=0

answer=float('inf')
ht=0

for i in range(0,266):
    check=False

    up=0
    down=0

    for j in range(N):
        for k in range(M):
            if(i-land[j][k]>0): #기준이 높아서 쌓아야 함.
                up+=i-land[j][k]
            elif(i-land[j][k]<0): # 기준이 낮아서 지워야 함.
                down+=abs(i-land[j][k])

    if(up>down+B):
        continue

    if(not check):
        if(answer>=up+down*2):
            answer=up+down*2  
            ht=i

print(answer,ht)