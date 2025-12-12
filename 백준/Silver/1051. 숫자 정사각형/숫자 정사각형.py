import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

square=[]
max_value=float('-inf')

for i in range(N):
    square.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(N-1):
    for j in range(M-1):
        for k in range(1,min(N-i,M-j)):
            if(square[i][j]==square[i+k][j]==square[i][j+k]==square[i+k][j+k]):
                max_value=max(k+1,max_value)

print(max_value**2 if max_value!=float('-inf') else 1)