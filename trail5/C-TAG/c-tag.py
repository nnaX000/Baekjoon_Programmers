from itertools import combinations

n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

candi=[i for i in range(m)]

sample=list(combinations(candi,3))

answer=0

for a,b,c in sample:
    A_s=set()
    B_s=set()
    check=False

    for i in range(n):
        A_s.add((A[i][a],A[i][b],A[i][c]))

    for i in range(n):
        if((B[i][a],B[i][b],B[i][c]) in A_s):
            check=True
            break

    if(not check):
        answer+=1

print(answer)