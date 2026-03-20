import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

tmp = 1
LOG = 1
while tmp <= N:
    tmp *= 2
    LOG += 1

pow2 = [1] * LOG
for i in range(1, LOG):
    pow2[i] = pow2[i - 1] * 2

parent = [[0 for _ in range(N + 1)] for _ in range(LOG)]
depth = [0 for _ in range(N + 1)]
visited = [False] * (N + 1)

dq = deque()
dq.append((1, 0))
visited[1] = True

# 각 노드의 바로 위 부모와 depth 구하기
while dq:
    cur, par = dq.popleft()
    parent[0][cur] = par

    for nxt in tree[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            depth[nxt] = depth[cur] + 1
            dq.append((nxt, cur))

# 스파스 테이블 구성
for k in range(1, LOG):
    for v in range(1, N + 1):
        mid = parent[k - 1][v]
        parent[k][v] = parent[k - 1][mid]

def lca(a, b):
    # b가 더 깊도록 맞춤
    if depth[a] > depth[b]:
        a, b = b, a

    diff = depth[b] - depth[a]

    # 깊이 맞추기
    for k in range(LOG - 1, -1, -1):
        if diff >= pow2[k]:
            b = parent[k][b]
            diff -= pow2[k]

    if a == b:
        return a

    # 같이 점프
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))