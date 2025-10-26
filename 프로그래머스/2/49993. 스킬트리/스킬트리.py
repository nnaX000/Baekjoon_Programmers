from collections import defaultdict
import copy

def solution(skill, skill_trees):
    sd_origin = defaultdict(int)
    count = 0
    answer = 0
    
    for i in range(len(skill)):
        sd_origin[skill[i]] = count
        count+=1
    
    sd = copy.deepcopy(sd_origin)
        
    for i in range(len(skill_trees)):
        possible = True
        sd = copy.deepcopy(sd_origin)
        for j in skill_trees[i]:
            if(j in sd and sd[j] != 0):
                possible = False
                break
            elif(j in sd and sd[j] == 0):
                for key,values in sd.items():
                    if(values>0):
                        values-=1
                        sd[key] = values
            
        if(possible):
            answer+=1
            
    return answer