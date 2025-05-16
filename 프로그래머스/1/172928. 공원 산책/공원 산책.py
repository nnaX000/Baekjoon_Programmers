def nav(direction, distance, present, park):
    sample=present.copy()
    if(direction=="N"):
        sample[0]-=distance
    elif(direction=="S"):
        sample[0]+=distance
    elif(direction=="W"):
        sample[1]-=distance
    elif(direction=="E"):
        sample[1]+=distance
    
    if(sample[0]<0 or sample[1]<0 or sample[0]>len(park)-1 or sample[1]>len(park[0])-1 or park[sample[0]][sample[1]]=="X"):
        return [-1000,-1000]
    else:
        return sample
    
def solution(park, routes):
    present=[0]*2
    for idx,i in enumerate(park):
        for idxx,j in enumerate(i):
            if(j=="S"):
                present[0]=idx
                present[1]=idxx
                break
                
    for i in routes :
        direction,distance=i.split(" ")
        distance=int(distance)
        certain_loc=present
        for j in range(distance):
            result=nav(direction,1,present,park)
            if(result==[-1000,-1000]):
                present=certain_loc
                break
            else:
                present=result
        

    return present