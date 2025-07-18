import sys

array=[]

x=0
y=0

board="WBWBWBWB"

min_value=[float('inf')]

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

for i in range(N):
    tmp=list(sys.stdin.readline().rstrip())
    array.append(tmp)

while(x<=N-8 and y<=M-8):
    result=0
    for i in range(8):
        board=''.join(reversed(board))
        for j in range(8):
            if(array[x+i][y+j]!=board[j]):
                result+=1

    if(result<min_value[0]):
        min_value[0]=result

    result=0

    for i in range(8):
        if(i!=0):
            board=''.join(reversed(board))
        for j in range(8):
            if(array[x+i][y+j]!=board[j]):
                result+=1

    if(result<min_value[0]):
        min_value[0]=result

    x+=1
    if(x==N-7):
        x=0
        y+=1


print(min_value[0])