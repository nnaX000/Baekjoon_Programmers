import sys

board=[[0 for i in range(9)] for j in range(9)]

x=0
y=0
max_value=0

for i in range(9):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    board[i]=tmp

for i in range(9):
    for j in range(9):
        if(max_value<=board[i][j]):
            x=i+1
            y=j+1
            max_value=board[i][j]

print(max_value)
print(x,y)