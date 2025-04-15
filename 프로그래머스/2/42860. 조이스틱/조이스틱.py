def solution(name):
    up_down_move = 0
    right_left_move = len(name) - 1
    
    for i, char in enumerate(name):
        up_down_move += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next=i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        right_left_move = min([right_left_move, 2*i + len(name) - next, i + 2* (len(name) - next) ])

    answer = up_down_move + right_left_move
    
    return answer