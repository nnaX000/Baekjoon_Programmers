import sys

# 옆에 있는 톱니바퀴와 맞닿은 톱니의 극이 다르면 B는 A 회전방향 반대로 회전
# 맞닿은 극이 같다면 회전X

# N극은 0, S극은 1
# 회전시킨 톱니바퀴 번호, 방향
# 1-> 시계 방향, -1->반시계 방향

one=list(map(int,sys.stdin.readline().rstrip()))
two=list(map(int,sys.stdin.readline().rstrip()))
three=list(map(int,sys.stdin.readline().rstrip()))
four=list(map(int,sys.stdin.readline().rstrip()))

tire=[]
tire.append([0,0,0,0,0,0,0,0])
tire.append(one)
tire.append(two)
tire.append(three)
tire.append(four)

noon=[0,0,0,0,0]

K=int(sys.stdin.readline().rstrip())

for i in range(K):
    number, direct = map(int,sys.stdin.readline().rstrip().split(' '))
    rotation=[False,False,False,False,False]
    direction=[0,0,0,0,0]

    rotation[number]=True
    direction[number]=direct

    previous=number
    next=number
    n_d=-direct

    #전
    while(previous>=2):
        if(tire[previous][noon[previous]-2]!=tire[previous-1][(noon[previous-1]+2)%8]):
            rotation[previous-1]=True
            direction[previous-1]=n_d
            n_d=-n_d
            previous-=1
        else:
            break

    n_d=-direct

    #후
    while(next<=3):
        if(tire[next][(noon[next]+2)%8]!=tire[next+1][noon[next+1]-2]):
            rotation[next+1]=True
            direction[next+1]=n_d
            n_d=-n_d
            next+=1
        else:
            break

    for j in range(1,len(rotation)):
        if(rotation[j]):
            if(direction[j]==-1):
                noon[j]=(noon[j]+1)%8
            else:
                noon[j]=noon[j]-1 if noon[j]-1>=0 else 7

answer=0

for i in range(1,len(noon)):
    if(tire[i][noon[i]]==1):
        if(i==1):
            answer+=1
        elif(i==2):
            answer+=2
        elif(i==3):
            answer+=4
        else:
            answer+=8

print(answer)