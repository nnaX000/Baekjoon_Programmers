def solution(schedules, timelogs, startday):
    #토,일 index가 각각 5랑 6/5-(startday-1),6-(startday-1)는 countX
    sature=5-(startday-1)
    if(sature==-1):
        sature=6
    sun=6-(startday-1)
    answer = 0

    for idx,i in enumerate(timelogs):
        discri=True
        deadline=schedules[idx]+10
        if(deadline%100>59):
            deadline=(100*(deadline//100+1))+(deadline%100-60)
        for idxx,j in enumerate(i):
            if(idxx!=sature and idxx!=sun):
                if(timelogs[idx][idxx]>deadline):
                    discri=False
                    break
        if(discri):
            answer+=1
    return answer