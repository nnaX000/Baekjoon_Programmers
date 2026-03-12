def solution(arr, delete_list):
    delete=set(delete_list)
    answer=[]
    for i in range(len(arr)):
        if(arr[i] not in delete):
            answer.append(arr[i])
    return answer