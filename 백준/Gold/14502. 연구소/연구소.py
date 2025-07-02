from collections import deque
import copy
import itertools

N,M=map(int,input().split(' '))

array=[]
zero=[]
virus=deque()
count=0
one=0
min_answer=[float('inf')]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def estimation(x,y):
    count=1
    
    for j in range(4):
        new_x=x+dx[j]
        new_y=y+dy[j]

        if(0<=new_x<N and 0<=new_y<M and test[new_x][new_y]==0):
            test[new_x][new_y]=2
            count+=estimation(new_x,new_y)
    
    return count

for i in range(N):
    array.append(list(map(int,input().split(' '))))

for i in range(N):
    for j in range(M):
        if(array[i][j]==2):
            virus.append([i,j])
        if(array[i][j]==0):
            zero.append([i,j])
        if(array[i][j]==1):
            one+=1

combinations=itertools.combinations(zero,3)

for i in combinations:
    test = copy.deepcopy(array)
    results=0
    count=0

    test[i[0][0]][i[0][1]]=1
    test[i[1][0]][i[1][1]]=1
    test[i[2][0]][i[2][1]]=1

    for k in virus:
        result=estimation(k[0],k[1])
        results+=result

    min_answer[0]=min(min_answer[0],results)

print((N*M)-min_answer[0]-(one+3))




