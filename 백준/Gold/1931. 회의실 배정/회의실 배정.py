import sys

N=int(sys.stdin.readline().rstrip())
conference=[]
max_value=1

for i in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    conference.append(tmp)

conference.sort(key=lambda x:x[0])
conference.sort(key=lambda x:x[1]) # 종료 시간 빠른순 정렬

stand=conference[0][1]

for i in range(1,len(conference)):
    if(conference[i][0]>=stand):
        stand=conference[i][1]
        max_value+=1

print(max_value)