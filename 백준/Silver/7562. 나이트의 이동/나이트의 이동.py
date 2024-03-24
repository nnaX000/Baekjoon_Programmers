import sys
from collections import deque
def BFS(myeon,start,target,visited):
    dx=[2,2,-2,-2,1,1,-1,-1]
    dy=[1,-1,1,-1,2,-2,2,-2]
    count=0
    dequee=deque()
    dequee.append(start)
    while(dequee):
        size=len(dequee)
        count+=1
        for i in range(size):
            stand=dequee.popleft()
            for j in range(8):
                check=True
                tmp=[stand[0]+dx[j],stand[1]+dy[j]]
                if(tmp[0]<0 or tmp[1]<0 or tmp[0]>=myeon or tmp[1]>=myeon):
                    continue
                if(tmp[0]==target[0] and tmp[1]==target[1]):
                    return count
                if(tuple(tmp) in visited):
                    check=False
                if(check):
                    visited.add(tuple(tmp))
                    dequee.append(tmp)

testcase=int(sys.stdin.readline())
answers=[]
for i in range(testcase):
    visited=set()
    myeon=int(input())
    start=list(map(int,sys.stdin.readline().split(' ')))
    target=list(map(int,sys.stdin.readline().split(' ')))
    if(target[0]==start[0] and start[1]==target[1]):
        answers.append(0)
    else:
        answer=BFS(myeon,start,target,visited)
        answers.append(answer)

for i in answers:
    print(i)