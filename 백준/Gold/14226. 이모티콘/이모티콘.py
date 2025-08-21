import sys
from collections import deque

S=int(sys.stdin.readline().rstrip())

#화면에 있는 임티 복사 , 클립보드 저장
#클립보드에 있는거 붙여넣기
#화면에 있는 이모티콘 중 하나 삭제

dequee=deque()
dequee.append([1,0,0])#[화면에 있는 임티 개수, 클립보드 임티 개수, 시간]
dist = [[-1]*(2000) for _ in range(2000)]

while(dequee):
    tmp=dequee.popleft()

    if(tmp[0]==S):
        print(tmp[2])
        break
    
    if(tmp[0]>0):
        if(0<=tmp[0]-1<2000 and dist[tmp[0]][tmp[0]]==-1):
            dequee.append([tmp[0],tmp[0],tmp[2]+1])
            dist[tmp[0]][tmp[0]]=tmp[2]+1
        if(dist[tmp[0]-1][tmp[1]]==-1):
            dequee.append([tmp[0]-1,tmp[1],tmp[2]+1])
            dist[tmp[0]-1][tmp[1]]=tmp[2]+1

    if(tmp[1]>0):
        if(0<=tmp[0]+tmp[1]<2000 and dist[tmp[0]+tmp[1]][tmp[1]]==-1):
            dequee.append([tmp[0]+tmp[1],tmp[1],tmp[2]+1])
            dist[tmp[0]+tmp[1]][tmp[1]]=tmp[2]+1