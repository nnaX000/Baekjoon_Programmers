from collections import deque
import itertools

def solution(picks, minerals):
    mineralss=deque(minerals)
    splited_minerals=[]
    tired=[[1,1,1],[5,1,1],[25,5,1]]
    carry=[]
    array=[]
    minn=0
    answer=[2000]
    
    #광물 5개씩 쪼개기
    while(len(mineralss)>0):
        if(len(array)==5):
            splited_minerals.append(array)
            array=[]
        else:
            temp=mineralss.popleft()
            array.append(temp)
            if(len(mineralss)==0):
                splited_minerals.append(array)
    
    def dfs(depth,tool,cost):
        if (depth==len(splited_minerals) or sum(tool)==0):
            answer[0]=min(answer[0],cost)
            return 
        else:
            for i in range(3):
                fatique=0
                if(tool[i]==0):
                    continue
                for j in splited_minerals[depth]:
                    if(j=="diamond"):
                        fatique+=tired[i][0]
                    elif(j=="iron"):
                        fatique+=tired[i][1]
                    else:
                        fatique+=tired[i][2]
                tool[i]-=1
                dfs(depth+1,tool,fatique+cost)
                tool[i]+=1
                
    dfs(0,picks,0)
    return answer[0]