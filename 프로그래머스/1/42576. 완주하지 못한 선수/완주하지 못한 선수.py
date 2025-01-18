def solution(participant, completion):
    answer = ''
    participants={}
    for i in participant:
        if(i in participants):
            participants[i]+=1
        else:
            participants[i]=1
    for j in completion:
        participants[j]-=1
        if(participants[j]==0):
            del participants[j]
    for key,value in participants.items():
        answer=key
    return answer 