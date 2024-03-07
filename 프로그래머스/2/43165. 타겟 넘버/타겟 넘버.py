def solution(numbers, target):
    answer = 0
    array=[[] for i in range(len(numbers))]
    for i in range(len(numbers)):
        temp=numbers[i]
        if(i==0):
            array[i].append(temp)
            array[i].append(-temp)
        else:
            for j in range(len(array[i-1])):
                array[i].append(array[i-1][j]+temp)
                array[i].append(array[i-1][j]-temp)
            
    answer=array[len(numbers)-1].count(target)
    return answer