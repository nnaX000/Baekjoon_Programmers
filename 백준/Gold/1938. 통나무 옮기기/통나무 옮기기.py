import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
logs=[]

B=[]
E=[]

check="g" # B통나무가 가로인지 세로인지 판별

garo=[[-1,0],[1,0]]
sero=[[0,-1],[0,1]]

for i in range(N):
    logs.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(N):
        if(logs[i][j]=="B"):
            B.append([i,j])
        elif(logs[i][j]=="E"):
            E.append([i,j])

if(B[0][0]==B[1][0]):
    check="g"
else:
    check="s"

dequee=deque()
dequee.append((B,0,check))

visited=set()
visited.add(tuple(tuple(i) for i in B))

while(dequee):
    B_array,cost,check=dequee.popleft()
    #print("나온 것",B_array)
    
    B_array.sort()

    if(B_array==E):
        print(cost)
        sys.exit(0)

    n_B=[i[:] for i in B_array]
    possible=True

    #상
    if(0<B_array[0][0]<N):
        for i in range(3):
            if(logs[B_array[i][0]-1][B_array[i][1]]!="1"):
                n_B[i][0]-=1
            else:
                possible=False
                break

    if(possible and tuple(tuple(i) for i in n_B) not in visited):
        visited.add(tuple(tuple(i) for i in n_B))
        #print("상에 넣습니다",n_B)
        dequee.append((n_B,cost+1,check))

    n_B=[i[:] for i in B_array]
    possible=True
    
    #하
    if(0<=B_array[2][0]<N-1):
        for i in range(3):
            if(logs[B_array[i][0]+1][B_array[i][1]]!="1"):
                n_B[i][0]+=1
            else:
                possible=False
                break

    if(possible and tuple(tuple(i) for i in n_B) not in visited):
        visited.add(tuple(tuple(i) for i in n_B))
        #print("하에 넣습니다",n_B)
        dequee.append((n_B,cost+1,check))

    n_B=[i[:] for i in B_array]
    possible=True

    #좌
    if(0<B_array[0][1]<N):
        for i in range(3):
            if(logs[B_array[i][0]][B_array[i][1]-1]!="1"):
                n_B[i][1]-=1
            else:
                possible=False
                break

    if(possible and tuple(tuple(i) for i in n_B) not in visited):
        visited.add(tuple(tuple(i) for i in n_B))
        #print("좌에 넣습니다",n_B)
        dequee.append((n_B,cost+1,check))

    n_B=[i[:] for i in B_array]
    possible=True

    #우
    if(0<=B_array[2][1]<N-1):
        for i in range(3):
            if(logs[B_array[i][0]][B_array[i][1]+1]!="1"):
                n_B[i][1]+=1
            else:
                possible=False
                break

    if(possible and tuple(tuple(i) for i in n_B) not in visited):
        visited.add(tuple(tuple(i) for i in n_B))
        #print("우에 넣습니다",n_B)
        dequee.append((n_B,cost+1,check))

    n_B=[i[:] for i in B_array]
    possible=True

    #회전
    if(check=="g"):
        for i in range(3):
            for j in range(2):
                if(0<=n_B[i][0]+garo[j][0]<N and 0<=n_B[i][1]+garo[j][1]<N and logs[n_B[i][0]+garo[j][0]][n_B[i][1]+garo[j][1]]!="1"):
                    possible=True
                else:
                    possible=False
                    break

            if(not possible):
                break

        if(possible):
            n_B[0][0],n_B[0][1]=n_B[1][0]-1,n_B[1][1]
            n_B[2][0],n_B[2][1]=n_B[1][0]+1,n_B[1][1]

        if(tuple(tuple(i) for i in n_B) not in visited):
            visited.add(tuple(tuple(i) for i in n_B))
            #print("회전g에 넣습니다",n_B)
            dequee.append((n_B,cost+1,"s"))

    else:
        for i in range(3):
            for j in range(2):
                if(0<=n_B[i][0]+sero[j][0]<N and 0<=n_B[i][1]+sero[j][1]<N and logs[n_B[i][0]+sero[j][0]][n_B[i][1]+sero[j][1]]!="1"):
                    possible=True
                else:
                    possible=False
                    break

            if(not possible):
                break

        if(possible):
            n_B[0][0],n_B[0][1]=n_B[1][0],n_B[1][1]-1
            n_B[2][0],n_B[2][1]=n_B[1][0],n_B[1][1]+1

        if(tuple(tuple(i) for i in n_B) not in visited):
            visited.add(tuple(tuple(i) for i in n_B))
            #print("회전s에 넣습니다",n_B)
            dequee.append((n_B,cost+1,"g"))

print(0)


# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33