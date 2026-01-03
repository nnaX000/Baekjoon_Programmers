import sys
from collections import Counter

input=sys.stdin.readline

N,M,B=map(int,input().split())
land=[list(map(int,input().split())) for _ in range(N)]
land_c=[i for j in land for i in j]
c=Counter(land_c)

#블록을 제거하는게 더 큰 cost -> 차라리 쌓는게 나음.
#땅 높이는 256블록 초과 X
#심을수있는 블록수 정해져있음

min_value=min(land_c)
max_value=max(land_c)

if(max_value>256):
    max_value=256

if(min_value<0):
    min_value=0

answer=float('inf')
ht=0

for i in range(min_value,max_value+1):
    up=0
    down=0

    for k,v in c.items():
        if(i-k>0): #기준이 높아서 쌓아야 함.
            up+=(i-k)*v
        elif(i-k<0): # 기준이 낮아서 지워야 함.
            down+=abs(i-k)*v

    if(up>down+B):
        continue

    if(answer>=up+down*2):
        answer=up+down*2  
        ht=i

print(answer,ht)