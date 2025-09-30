from collections import defaultdict

def solution(friends, gifts):
    given = defaultdict(lambda: defaultdict(int)) # 놓친 부분 : 딕셔너리 안에 딕셔너리
    taken = defaultdict(lambda: defaultdict(int))
    
    n_gifts=[]
    answer = defaultdict(int)

    for i in gifts:
         a,b=i.split(' ')
         n_gifts.append([a,b])
    
    for give, take in n_gifts:
        given[give][take]+=1
        taken[take][give]+=1
        
    for i in range(len(friends)-1):
        for j in range(i+1,len(friends)):
            
            if ((given[friends[i]][friends[j]] != 0 or given[friends[j]][friends[i]] != 0) and given[friends[i]][friends[j]] != given[friends[j]][friends[i]]):
                
                if(given[friends[i]][friends[j]] > given[friends[j]][friends[i]]):
                    answer[friends[i]]+=1
                else:
                    answer[friends[j]]+=1
            #두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 
            elif ((given[friends[i]][friends[j]] == 0 and given[friends[j]][friends[i]] == 0) or (given[friends[i]][friends[j]] == given[friends[j]][friends[i]])):
                 
                 if(sum(given[friends[i]].values())-sum(taken[friends[i]].values())>sum(given[friends[j]].values())-sum(taken[friends[j]].values())): # 놓친 부분 : 딕셔너리에서 값 기준으로 합 구하는 법
                        answer[friends[i]]+=1
                 elif(sum(given[friends[i]].values())-sum(taken[friends[i]].values())<sum(given[friends[j]].values())-sum(taken[friends[j]].values())):
                        answer[friends[j]]+=1
                        
    answer = max(answer.values()) if answer else 0
    return answer
