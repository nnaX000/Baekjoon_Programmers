import sys

score=[]
player=[]
min_value=[float('inf')]

N=int(sys.stdin.readline().rstrip())

for i in range(N):
    score.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

for i in range(N):
    player.append(i)

team=[]
result=[]
visited=[False for i in range(len(player))]

def dfs(visited,start):
    if(len(team)==N//2):
        result.append(team[:])
        
    for i in range(start,len(player)):
        if(visited[i]):
            continue
        visited[i]=True
        team.append(i)
        dfs(visited,i+1)
        visited[i]=False
        team.pop()

dfs(visited,0)

for i in result:
    one=0
    two=0
    ex=[]
    for j in range(N):
        if(j not in i):
            ex.append(j)

    for jdx,j in enumerate(i):
        for k in range(jdx+1,len(i)):
            one+=score[j][i[k]]
            one+=score[i[k]][j]

    for jdx,j in enumerate(ex):
        for k in range(jdx+1,len(ex)):
            two+=score[j][ex[k]]
            two+=score[ex[k]][j]

    if(abs(one-two)<min_value[0]):
        min_value[0]=abs(one-two)

print(min_value[0])