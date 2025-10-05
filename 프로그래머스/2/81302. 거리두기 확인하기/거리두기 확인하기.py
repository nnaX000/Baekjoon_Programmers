def solution(places):
    answer = []
    
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])
    
    #거리가 1인 상하좌우
    basic_dx = [-1,1,0,0]
    basic_dy = [0,0,-1,1]
    
    #거리가 2인 상하좌우
    two_strict_dx = [-2,2,0,0]
    two_strict_dy = [0,0,-2,2]
    check_strict_dx = [-1,1,0,0]
    check_strict_dy = [0,0,-1,1]
    
    
    #거리가 2인 대각선
    two_dx = [-1,-1,1,1]
    two_dy = [-1,1,-1,1]
    check_two_dx = [[-1,0],[-1,0],[0,1],[0,1]]
    check_two_dy = [[0,-1],[0,1],[-1,0],[1,0]]
    
    for i in range(5):
        check = False
        for j in range(5):
            for k in range(5):
                if(places[i][j][k] == "P"):
                    
                    # 상하좌우 보기
                    for l in range(4):
                        n_dx = j+basic_dx[l]
                        n_dy = k+basic_dy[l]
                        if(0<=n_dx<5 and 0<=n_dy<5 and places[i][n_dx][n_dy] == "P"):
                            check = True
                            break
                            
                    if(check):
                        break
                            
                    # 거리가 2인 상하좌우 보기
                    for l in range(4):
                        n_dx = j+two_strict_dx[l]
                        n_dy = k+two_strict_dy[l]
                        check_dx = j+check_strict_dx[l]
                        check_dy = k+check_strict_dy[l]
                        
                        if(0<=n_dx<5 and 0<=n_dy<5 and places[i][n_dx][n_dy] == "P"):
                            if(places[i][check_dx][check_dy] != "X"):
                                check = True
                                break
                                
                    if(check):
                        break
                                
                    #거리가 2인 대각선 보기
                    for l in range(4):
                        n_dx = j+two_dx[l]
                        n_dy = k+two_dy[l]
                        
                        if(0<=n_dx<5 and 0<=n_dy<5 and places[i][n_dx][n_dy] == "P"):
                            for o in range(2):
                                x_count = j+check_two_dx[l][o]
                                y_count = k+check_two_dy[l][o]
                                
                                if(0<=x_count<5 and 0<=y_count<5 and places[i][x_count][y_count] != "X"):
                                    check = True
                                    break
                                    
                        if(check):
                            break
                    if(check):
                        break
                if(check):
                    break
            if(check):
                break
        
        if (not check):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer