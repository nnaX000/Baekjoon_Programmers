from collections import defaultdict,deque

N, G = map(int, input().split())

# N명의 사람, G개의 그룹
# 1번 사람한테는 무조건 초대장을 줌.
# 확실히 초대장을 받게 되는 인원수

group = []

answer=1

visited=set()
assign=defaultdict(list)

dq=deque()

for i in range(G):
    arr = list(map(int, input().split()))
    num = arr[0]
    arr = arr[1:]
    group.append(arr)

    for j in arr:
        assign[j].append(i) # 1이 그룹 2번째에 속해있다.

dq.append(1) # 1은 이미 초대되었음.
visited.add(1)

while(dq):
    tmp=dq.popleft()

    for i in assign[tmp]:
        count=0
        target=0

        for j in group[i]:
            if(j not in visited):
                count+=1
                target=j
            
            if(count>=2):
                break

        if(count==1):
            #print("target",target)
            answer+=1
            visited.add(target)
            dq.append(target)

print(answer)