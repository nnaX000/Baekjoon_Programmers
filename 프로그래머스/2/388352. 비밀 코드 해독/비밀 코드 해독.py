from itertools import combinations

def solution(n, q, ans):
    answer = 0
    candi = []
    for i in range(1,n+1):
        candi.append(i)
    for i in combinations(candi,5):
        check=True
        for jdx,j in enumerate(q):
            tmp = set(j) & set(i)
            if(len(tmp)!=ans[jdx]):
                check=False
                break
        if(check):
            answer+=1
    return answer