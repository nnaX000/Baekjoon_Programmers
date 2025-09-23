import sys
import itertools

N,M,K = map(int,sys.stdin.readline().rstrip().split(' '))
A = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(N)]
min_value=float('inf')
calcul=[]

for i in range(K):
    calcul.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

for i in itertools.permutations(calcul,len(calcul)):

    B=[k[:] for k in A]

    for j in i:
        r=j[0]
        c=j[1]
        s=j[2]

        first = [r-s,c-s] # first랑 end는 인덱스 1부터 시작
        end = [r+s,c+s]
        size = (2*s+1) ** 2

        x= first[0]-1 # x랑 y는 실인덱스
        y= first[1]-1
        tmp= B[x][y]
        check=True

        while(size>=4 or check) : 
            check = True

            if ((x==first[0]-1) and y+1<=end[1]-1):
                pocket = B[x][y+1]
                B[x][y+1] = tmp
                tmp = pocket

                y+=1
            elif ((y==end[1]-1) and x+1<=end[0]-1):
                pocket = B[x+1][y]
                B[x+1][y] = tmp
                tmp = pocket

                x+=1
            elif (x==end[0]-1 and y-1>=first[1]-1):
                pocket = B[x][y-1]
                B[x][y-1] = tmp
                tmp = pocket

                y-=1
            elif (y==first[1]-1 and x-1>=first[0]-1):
                pocket = B[x-1][y]
                B[x-1][y] = tmp
                tmp = pocket

                x-=1

            if(x==first[0]-1 and y==first[1]-1):
                check=False
                x+=1
                y+=1
                first=[first[0]+1,first[1]+1]
                end=[end[0]-1,end[1]-1]
                tmp= B[x][y]
            
            size-=1

    for i in B:
        sum_value=sum(i)
        min_value=min(sum_value,min_value)


print(min_value)