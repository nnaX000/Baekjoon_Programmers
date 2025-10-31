def solution(board):
    answer = 0
    
    row = len(board)
    column = len(board[0])
    
    
    for i in range(row):
        for j in range(column):
            if(board[i][j]==1):
                if(i!=0 and j!=0):
                    board[i][j]=min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                    
                answer=max(answer,board[i][j])
                    
    return answer*answer