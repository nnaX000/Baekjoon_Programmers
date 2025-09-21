import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
ban_matrix = [[False]*(N+1) for _ in range(N+1)]
answer=0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ban_matrix[a][b] = True
    ban_matrix[b][a] = True

for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if not (ban_matrix[i][j] or ban_matrix[i][k] or ban_matrix[j][k]):
                answer+=1

print(answer)