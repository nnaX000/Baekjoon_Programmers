import sys
input = sys.stdin.readline
MOD = 1000000007

M = int(input())
ans = 0

for _ in range(M):
    N, S = map(int, input().split())
    ans = (ans + S * pow(N, MOD-2, MOD)) % MOD

print(ans)