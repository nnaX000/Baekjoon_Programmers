# 0 빈칸 / 1 집 / 2 치킨칩
# NxN
# M은 고를 수 있는 치킨집 수

import sys
import itertools

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

village=[]
result=[]
chicken=[]
path=[]
home=[]
answer=[float('inf')]

for i in range(N):
    village.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

for i in range(N):
    for j in range(N):
        if(village[i][j]==2):
            chicken.append([i,j])
        if(village[i][j]==1):
            home.append([i,j])

visited=[False for i in range(len(chicken))]

# def dfs(chicken,visited,path,start):
#     if(len(path)==M):
#         result.append(path[:])
#         return
    
#     for i in range(start,len(chicken)):
#         if(visited[i]):
#             continue

#         path.append(chicken[i])
#         visited[i]=True
#         dfs(chicken,visited,path,start+1)
#         visited[i]=False
#         path.pop()

# dfs(chicken,visited,path,0)

result=itertools.combinations(chicken, M)

for i in result:
    sum_value=0
    for j in home:
        min_value=[float('inf')]
        for k in i:
            tmp=abs((k[0]+1)-(j[0]+1))+abs((k[1]+1)-(j[1]+1))
            if(tmp<min_value[0]):
                min_value[0]=tmp
        sum_value+=min_value[0]
    
    if(sum_value<answer[0]):
        answer[0]=sum_value

print(answer[0])