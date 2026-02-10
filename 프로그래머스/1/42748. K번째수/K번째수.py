def solution(array, commands):
    answer = []
    for l in range(len(commands)):
        i,j,k=commands[l][0],commands[l][1],commands[l][2]
        tmp=array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer