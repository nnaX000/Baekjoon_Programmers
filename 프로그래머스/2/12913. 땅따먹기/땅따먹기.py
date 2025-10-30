def solution(land):
    answer = float('-inf')
    length = len(land)
    
    for i in range(1,length):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[length-1])