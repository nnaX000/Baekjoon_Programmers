import sys
from collections import deque

S=int(sys.stdin.readline().rstrip())

#화면에 있는 임티 복사 , 클립보드 저장
#클립보드에 있는거 붙여넣기
#화면에 있는 이모티콘 중 하나 삭제

dequee=deque()
dequee.append([1,0])#[화면에 있는 임티 개수, 클립보드 임티 개수]
dist = [[-1]*(2000) for _ in range(2000)]
dist[1][0]=0

while(dequee):
    s,c=dequee.popleft()
    t=dist[s][c]

    if(s==S):
        print(dist[s][c])
        break
    
    #화면에 있는 임티 복사
    if(dist[s][s]==-1):
        dequee.append([s,s])
        dist[s][s]=t+1

    #클립보드에 있는거 붙여넣기
    if(c>0 and 0<=s+c<2000 and dist[s+c][c]==-1):
        dequee.append([s+c,c])
        dist[s+c][c]=t+1

    #화면에 있는 이모티콘 중 하나 삭제
    if((s>0) and 0<=s-1<2000 and dist[s-1][c]==-1):
        dequee.append([s-1,c])
        dist[s-1][c]=t+1