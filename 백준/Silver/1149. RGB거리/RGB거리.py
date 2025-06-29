N=int(input())
array=[]

for i in range(N):
    array.append(list(map(int,input().split(' '))))

table=[[0 for i in range(3)] for j in range(N)]

for i in range(3):
    table[0][i]=array[0][i]

for i in range(1,N):
    for j in range(3):
        if(j==0):
            table[i][j]=min(array[i][j]+table[i-1][1],array[i][j]+table[i-1][2])
        elif(j==1):
            table[i][j]=min(array[i][j]+table[i-1][0],array[i][j]+table[i-1][2])
        else:
            table[i][j]=min(array[i][j]+table[i-1][0],array[i][j]+table[i-1][1])

print(min(table[N-1]))
