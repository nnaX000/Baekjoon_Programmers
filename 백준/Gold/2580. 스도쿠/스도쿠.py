import sys
from collections import Counter
import copy

sdoku=[]
answer=[]

for i in range(9):
    sdoku.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

def dfs():
    
    for i in range(9):#이 for문은 재귀적으로 다 마무리 되고 이제 다 채워졌나 보는 용도
        for j in range(9):
            if(sdoku[i][j]==0):
                total=set(range(0,10))
                total-=set(sdoku[i])
                for k in range(9):
                    total.discard(sdoku[k][j])
                box_x=(i//3)*3
                box_y=(j//3)*3
                for k in range(box_x,box_x+3):
                    for m in range(box_y,box_y+3):
                        total.discard(sdoku[k][m])
                for k in total:
                    sdoku[i][j]=k
                    dfs() #dfs를 통해 다음 칸들을 되는 조합으로 미리 채우는 중
                    sdoku[i][j]=0 #이걸 해줘야 실패하고 다시 돌아왔을때 if(sdoku[i][j]==0): 이 조건에 위반되지 않아 정상적으로 나머지 for문을 돌릴 수 있음
                return#처음 0을 만났을때 재귀적으로 성공해서 모든 수를 찾아온 경우는 다시 if문으로 안돌아오기 때문에 return 될 일이 없음
                

    for row in sdoku:
        print(' '.join(map(str, row)))
    sys.exit(0)

dfs() 