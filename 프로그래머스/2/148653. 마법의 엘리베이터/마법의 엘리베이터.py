def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10  # 현재 자리
        next_digit = (storey // 10) % 10  # 다음 자리 (올림 판단용)
        
        if digit > 5:  # 6~9면 올림하는 게 유리
            answer += 10 - digit
            storey += 10
        elif digit < 5:  # 0~4면 그냥 내리는 게 유리
            answer += digit
        else:  # digit == 5
            # 다음 자리수가 5 이상이면 올림, 아니면 내림
            if next_digit >= 5:
                answer += 10 - digit
                storey += 10
            else:
                answer += digit
                
        storey //= 10  # 다음 자리로 이동
        
    return answer