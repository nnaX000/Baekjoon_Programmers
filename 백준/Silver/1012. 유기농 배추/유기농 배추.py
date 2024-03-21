#    01
#10  11  12
#    21
#node=[방문했으면 True,안했으면 False]
import sys
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]
testCaseNum=int(sys.stdin.readline())
answer=[]
for i in range(testCaseNum):
    count=0
    dequee = deque()
    garo,sero,where=map(int,sys.stdin.readline().split(' '))
    array = [[0 for i in range(sero+1)] for j in range(garo+1)]
    for j in range(where):
        tmp=list(map(int,sys.stdin.readline().split(' ')))
        array[tmp[0]][tmp[1]]=1
    for k in range(garo):
        for i in range(sero):
            if(array[k][i]==1):
                count+=1
                dequee.append([k,i])
                array[k][i]=0
                while(dequee):
                    start = dequee.popleft()
                    for i in range(4):
                        targetX = start[0] + dx[i]
                        targetY = start[1] + dy[i]
                        if (targetX < 0 or targetY < 0 or targetX >= garo or targetY >= sero):
                            continue
                        if (array[targetX][targetY] == 1):
                            dequee.append([targetX, targetY])
                            array[targetX][targetY] = 0

    answer.append(count)

for i in answer:
    print(i)

