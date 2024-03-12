def solution(N, number):
    answer = 0
    dp=[set() for i in range(8)]
    for i in range(len(dp)):
        dp[i].add(int(str(N)*(i+1)))
    #print(dp)
    for i in range(1,len(dp)):
        for j in range(i):
            for l in dp[j]:
                for k in dp[i-j-1]:
                    dp[i].add(l+k)
                    dp[i].add(l-k)
                    dp[i].add(l*k)
                    if(k!=0):
                        dp[i].add(l//k)
    #print(dp)
    for idx,i in enumerate(dp):
        if(number in i):
            answer=idx+1
            break
        else:
            answer=-1
    return answer