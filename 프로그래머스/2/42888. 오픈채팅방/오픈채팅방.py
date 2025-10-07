from collections import defaultdict

def solution(record):
    answer = []
    nickname = defaultdict(str)
    
    for i in range(len(record)):
        if(record[i][0] == "E" or record[i][0] == "C"):
            action, user_id, name = record[i].split(' ')
            nickname[user_id] = name
    
    for i in range(len(record)):
        if(record[i][0] == "E"):
            action, user_id, tmp = record[i].split(' ')
            answer.append(nickname[user_id]+"님이 들어왔습니다.")
        elif(record[i][0] == "L"):
            action, tmp = record[i].split(' ')
            answer.append(nickname[tmp]+"님이 나갔습니다.")
            
    return answer