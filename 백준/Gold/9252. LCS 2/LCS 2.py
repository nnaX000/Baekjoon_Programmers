import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

n, m = len(S), len(T)

# dp[i][j] = LCS length of S[:i] and T[:j]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    si = S[i - 1]
    for j in range(1, m + 1):
        if si == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # max(dp[i-1][j], dp[i][j-1])
            if dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

# 길이 출력
lcs_len = dp[n][m]
print(lcs_len)

# 문자열 복원 (역추적)
if lcs_len > 0:
    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            ans.append(S[i - 1])
            i -= 1
            j -= 1
        else:
            # 값이 큰 쪽으로 이동
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    ans.reverse()
    print(''.join(ans))