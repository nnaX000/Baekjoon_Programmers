import sys
from collections import defaultdict

#r은 위에서 떨어진 칸 수, c는 왼족으로부터 떨어진 칸 수
#r,c는 1부터 시작
#처음에 양분은 모든칸에 5만큼

#한칸에 여러개 나무가 심어져있을 수도..

#봄 -> 나이만큼 양분 먹고 나이 1 증가
#여름 -> 각각 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가 소수점 아래 버림
#가을 -> 번식하는 나무는 나이가 5의 배수, 인접한 8개 칸에 나이가 1인 나무 생김
#겨울 -> 각 땅에 양분 추가

N,M,K=map(int,sys.stdin.readline().rstrip().split(' ')) # K년

answer=0

land=[[5 for i in range(N)] for j in range(N)]

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

A=[]
for i in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    A.append(tmp)

trees=defaultdict(list)
for i in range(M):
    x,y,age=map(int,sys.stdin.readline().rstrip().split(' '))
    trees[(x-1,y-1)].append(age)

for key,value in trees.items():
    value.sort()

surround=defaultdict(list)

for i in range(N):
    for j in range(N):
        for k in range(8):
            n_x=i+dx[k]
            n_y=j+dy[k]

            if(0<=n_x<N and 0<=n_y<N):
                surround[(i,j)].append((n_x,n_y))


for i in range(K):
    #tmp=defaultdict(list)

    #봄 여름 합치기
    for key,value in trees.items():
        check=False
        x,y=key[0],key[1]
        tmp=[]
        value.sort()

        for j in value:
            if(not check):
                if(land[x][y]-j<0):
                    check=True
                    land[x][y]+=(j//2)
                else:
                    land[x][y]-=j
                    tmp.append(j+1)
            else:
                land[x][y]+=(j//2)

        trees[key]=tmp[:]

    tmp=defaultdict(list)
    num=defaultdict(int)

    #가을
    for key,value in trees.items():
        x,y=key[0],key[1]

        for j in value:
            if(j%5==0):
                num[key]+=1

    for key,value in surround.items():
        for j in value:
            for k in range(num[key]):
                trees[j].append(1)
    
    #겨울
    for j in range(N):
        for k in range(N):
            land[j][k]+=A[j][k]

for i in trees.values():
    answer+=len(i)

print(answer)