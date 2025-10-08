def solution(X, Y):
    countX = [0]*10
    countY = [0]*10
    
    for ch in X:
        countX[int(ch)] += 1
    for ch in Y:
        countY[int(ch)] += 1
    
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(countX[i], countY[i])
    
    if not answer:
        return "-1"
    if answer[0] == '0':
        return "0"
    return answer