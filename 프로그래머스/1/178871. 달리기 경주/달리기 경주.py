def solution(players, callings):
    answer = []
    dict={name:rank for rank,name in enumerate(players)}
    
    for i in callings:
        overtake=dict[i] #등수
        overtaken=players[overtake-1] #뺏기는애 이름
        
        players[overtake],players[overtake-1]=players[overtake-1],players[overtake]
        
        dict[i]=overtake-1
        dict[overtaken]=overtake
    
    return players