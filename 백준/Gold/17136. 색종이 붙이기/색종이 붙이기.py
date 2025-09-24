import sys

paper=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(10)]

color_paper=[0,5,5,5,5,5]
min_value=float('inf')

def dfs(color_paper,answer,n_x,n_y,paper):
    global min_value

    if sum(sum(row) for row in paper) == 0:
        min_value=min(answer,min_value)

    if(min_value<=answer):
        return

    for i in range(n_x,10):
        for j in range(n_y if i==n_x else 0,10):

            chance=True

            if(paper[i][j]==1):
                for k in range(5,0,-1):
                    if(color_paper[k]>0):
                        chance = True
                        nx = i
                        for l in range(k):
                            ny=j
                            for o in range(k):
                                if(0<=nx<10 and 0<=ny<10 and paper[nx][ny]==0):
                                    chance=False
                                    break
                                elif(not(0<=nx<10 and 0<=ny<10)):
                                    chance=False
                                    break
                                ny+=1
                            nx+=1

                            if(not chance):
                                break
                        
                        #되면 붙여줌
                        if(chance):
                            nx = i
                            for l in range(k):
                                ny=j
                                for o in range(k):
                                    paper[nx][ny]=0
                                    ny+=1
                                nx+=1

                            color_paper[k]-=1
                            answer+=1

                            n_x=i
                            n_y=j+1
                        
                            dfs(color_paper, answer, n_x, n_y, paper)
                            
                            #백트래킹
                            nx = i
                            for l in range(k):
                                ny=j
                                for o in range(k):
                                    paper[nx][ny]=1
                                    ny+=1
                                nx+=1

                            color_paper[k]+=1
                            answer-=1

                return
                             
dfs(color_paper,0,0,0,paper)

print(min_value if min_value!=float('inf') else -1)

#놓친 부분 
# 1. 백트래킹을 이용한 완전탐색으로 갔어야..나는 처음에 그리디로 했음. 순서대로 돌면서 가장 큰 색종이를 부여하는게 최적이 아님.
# 2. dfs 돌기 시작하면 처음부터 탐색하지 말고 다음 인덱스 넘겨서 거기서부터.
# 3. visited를 따로 두지 말고 paper로 0/1해서 방문여부 관리
# 4. 1인 인덱스를 여러군데 보지 말고 그냥 하나 처리해서 재귀로 넘기면 그 경우는 return
