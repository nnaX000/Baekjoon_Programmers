import sys
from itertools import combinations

array=[]

N=int(sys.stdin.readline().rstrip())
sum_value=0

for i in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    array.append(tmp)
    sum_value+=sum(tmp)

min_value=[float('inf')]

players=[i for i in range(N)]

def dfs(start,tmp):
    global min_value

    if(len(tmp)>=1):
        tmp_2=[i for i in range(N) if i not in tmp]
        team_one = sum(array[a][b] + array[b][a] for a, b in combinations(tmp, 2))
        team_two = sum(array[a][b] + array[b][a] for a, b in combinations(tmp_2, 2))
        # for i in range(N):
        #     for j in range(N):
        #         if(i==j):
        #             continue
        #         elif(i in tmp and j in tmp):
        #             team_one+=array[i][j]
        #         elif(i not in tmp and j not in tmp):
        #             team_two+=array[i][j]

        if(abs(team_one-team_two)<min_value[0]):
            min_value[0]=abs(team_one-team_two)

    if(len(tmp)>=N//2):
        return

    for i in range(start,len(players)):
        tmp.append(players[i])
        dfs(i+1,tmp)
        tmp.pop()


tmp=[]
dfs(0,tmp)

print(min_value[0])