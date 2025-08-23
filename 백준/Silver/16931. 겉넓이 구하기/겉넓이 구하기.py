import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

cube=[]

total=0

for i in range(N):
    cube.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

total+=(N*M)*2

stand=0
stand_reverse=0

#좌우(정방향/거꾸로)
for i in cube:
    stand=i[0]
    total+=i[0]
    stand_reverse=i[-1]
    total+=i[-1]
    for j in i:
        if(j>stand):
            total+=(j-stand)
        stand=j

    for j in reversed(i):
        if(j>stand):
            total+=(j-stand)
        stand=j

#상하(정방향/거꾸로)
for i in range(M):
    stand=cube[0][i]
    total+=cube[0][i]
    stand_reverse=cube[-1][i]
    total+=cube[-1][i]
    for j in range(N):
        if(stand<cube[j][i]):
            total+=(cube[j][i]-stand)
        stand=cube[j][i]

    for j in range(N-1,-1,-1):
        if(stand<cube[j][i]):
            total+=(cube[j][i]-stand)
        stand=cube[j][i]

print(total)