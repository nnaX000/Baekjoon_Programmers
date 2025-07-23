import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []

for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            chicken.append((i, j))
        elif village[i][j] == 1:
            home.append((i, j))

answer = float('inf')

for comb in combinations(chicken, M):
    sum_value = 0
    for hx, hy in home:
        min_dist = float('inf')
        for cx, cy in comb:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        sum_value += min_dist
    answer = min(answer, sum_value)

print(answer)