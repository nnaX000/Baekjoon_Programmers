# 3K번에 걸쳐 자리바꿈이 진행될 동안, 각자 몇 군데의 자리에 앉을 수 있는지
from collections import defaultdict

n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

seats = defaultdict(set)

current=[i for i in range(1,n+1)]

for i in range(1,n+1):
    seats[i].add(i)

for i in range(3):
    for a,b in edges:
        tmp=current[a-1]
        tmp_1=current[b-1]

        seats[tmp].add(b)
        seats[tmp_1].add(a)

        current[b-1]=tmp
        current[a-1]=tmp_1

for k,v in seats.items():
    print(len(v))