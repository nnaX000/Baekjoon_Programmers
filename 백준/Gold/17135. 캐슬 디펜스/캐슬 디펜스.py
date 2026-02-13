import sys
import heapq

input=sys.stdin.readline

N,M,D=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
enemy=[]
answer=float('-inf')

for i in range(N):
    for j in range(M):
        if(board[i][j]==1):
            enemy.append([i,j])

#0은 빈칸, 1은 적
#각 칸에는 적 최대 한명
#거리가 D인 적 중 가장 가까운 적 중 가장 왼쪽에 있는 적 공격
#궁수 3명 배치
#적이 아래 한칸씩 이동해서 성 있는 칸으로 이동하면 게임에서 제외

#궁수 어디에 배치할지 정하기
candi=[i for i in range(M)]
method=[]

def dfs(start,arr):
    global method

    if(len(arr)==3):
        method.append(arr[:])
        return
    
    for i in range(start,len(candi)):
        arr.append(candi[i])
        dfs(i+1,arr)
        arr.pop()

dfs(0,[])

for i in range(len(method)):
    arrow=method[i] # 현재 궁수들 위치. x축은 N으로 고정
    removed=0
    t_enemy=[j[:] for j in enemy]

    while(len(t_enemy)>0):
        remove=set()

        for j in range(3): # 각 궁수별로 쏠 대상 정하기
            heap=[]
            heapq.heapify(heap)
            for k in range(len(t_enemy)):
                e_x,e_y=t_enemy[k][0],t_enemy[k][1]
                distance=abs(e_x-N)+abs(e_y-arrow[j])

                heapq.heappush(heap,(distance,e_y,e_x))

            target=heapq.heappop(heap)
            if(target[0]<=D):
                remove.add((target[2],target[1]))

        #print(remove)
        removed+=len(remove)
        r_enemy=[]
        #궁수들이 겨냥한 적 없애기 및 적 이동
        for j in range(len(t_enemy)):
            if(tuple(t_enemy[j]) not in remove):
                if(t_enemy[j][0]+1<=N-1):
                    r_enemy.append([t_enemy[j][0]+1,t_enemy[j][1]])

        t_enemy=[j[:] for j in r_enemy]

    answer=max(answer,removed)

print(answer)   