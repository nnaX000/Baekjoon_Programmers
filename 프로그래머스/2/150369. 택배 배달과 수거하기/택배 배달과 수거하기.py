def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 처리해야 할 배달과 수거 상자의 '누적' 개수
    # 먼 곳의 일을 처리하려면 어차피 거쳐가야 하므로, 
    # 특정 지점에서는 그보다 먼 곳들의 남은 일을 모두 가지고 있다고 생각할 수 있음
    deliver_count = 0
    pickup_count = 0
    
    # 가장 먼 집부터 역순으로 탐색
    for i in range(n - 1, -1, -1):
        # 현재 집에서 처리해야 할 배달/수거량을 누적값에 더함
        deliver_count += deliveries[i]
        pickup_count += pickups[i]
        
        # 현재 위치에서 처리해야 할 배달 또는 수거가 남아있는 동안 반복
        # 예: 배달할 상자가 7개인데 cap이 5라면, 이 위치는 최소 2번 방문해야 함
        while deliver_count > 0 or pickup_count > 0:
            # 트럭이 한 번 왕복하면서 배달/수거 용량만큼 처리
            deliver_count -= cap
            pickup_count -= cap
            
            # 이 위치(i)를 방문해야만 했으므로 왕복 거리를 더해줌
            # (i+1)은 집의 번호이자 거리
            answer += (i + 1) * 2
            
    return answer