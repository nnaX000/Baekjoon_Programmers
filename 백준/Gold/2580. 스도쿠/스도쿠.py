import sys

sdoku=[]

for i in range(9):
    sdoku.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

def dfs(sdoku,start_x,start_y):

    for i in range(start_x,9):
        for j in range(start_y if i==start_x else 0,9):
            if(sdoku[i][j]==0):
                range_x=i-(i%3)
                range_y=j-(j%3)

                candidate=set(sdoku[i])
                candidate |= set([sdoku[r][c] for r in range(range_x, range_x + 3) for c in range(range_y, range_y + 3)])
                candidate |= set([row[j] for row in sdoku])

                for k in range(1,10):
                    if(k not in candidate):
                        sdoku[i][j]=k
                        nstart_x=i
                        nstart_y=j+1
                        if(nstart_y>8):
                            nstart_x=i+1
                            nstart_y=0

                        dfs(sdoku,nstart_x,nstart_y)

                        sdoku[i][j]=0   
                
                return

    for i in sdoku:
        print(*i)
    
    sys.exit(0)

dfs(sdoku,0,0) 