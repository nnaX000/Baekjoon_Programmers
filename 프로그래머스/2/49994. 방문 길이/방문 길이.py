def solution(dirs):
    answer = 0
    total = 0
    visited = set()
    
    x=0
    y=0
    
    for i in range(len(dirs)):
        if(dirs[i]=="U"):
            nx=x-1
            ny=y
        elif(dirs[i]=="D"):
            nx=x+1
            ny=y
        elif(dirs[i]=="R"):
            nx=x
            ny=y+1
        else:
            nx=x
            ny=y-1
            
        if(not (-5<=nx<=5) or not(-5<=ny<=5)):
            continue
            
        if((x,y,nx,ny) not in visited):
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
        else:
            answer+=1
        
        total+=1
        x=nx
        y=ny
    
    return total-answer