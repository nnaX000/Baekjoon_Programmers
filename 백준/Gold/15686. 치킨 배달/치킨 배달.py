import sys
from itertools import combinations
from collections import defaultdict

input=sys.stdin.readline

#0빈칸
#1집
#2치킨집
#최대 M개의 치킨집 고르기
#도시의 치킨 거리=모든 집의 치킨 거리 합

N,M=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(N)]
chicken=[]
house=[]

cost=defaultdict(list)

for i in range(N):
    for j in range(N):
        if(city[i][j]==2):
            chicken.append([i,j])
        elif(city[i][j]==1):
            house.append([i,j])

out=len(chicken)-M

for x,y in chicken:
    for h_x,h_y in house:
        cost[(h_x,h_y)].append(abs(h_x-x)+abs(h_y-y))

candi=[i for i in range(len(chicken))]
answer=float('inf')

for i in combinations(candi,out):
    except_c=set(i)
    tmp=0
    for key,value in cost.items():
        min_value=float('inf')
        for jdx,j in enumerate(value):
            if(jdx not in except_c):
                min_value=min(min_value,j)
        
        tmp+=min_value

    answer=min(answer,tmp)

print(answer)