def solution(strs, t):
    n = len(t)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    sset = set(strs) 

    for i in range(1, n + 1):
        for l in range(1, 6):  # 단어 최대 길이 5
            if i - l >= 0 and t[i-l:i] in sset:
                dp[i] = min(dp[i], dp[i-l] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1