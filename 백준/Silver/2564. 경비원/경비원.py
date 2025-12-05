import sys

answer=0

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

#1은 북쪽, 2는 남쪽, 3은 서쪽, 4는 동쪽
n=int(sys.stdin.readline().rstrip())
store=[]

for i in range(n):
    store.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

monitor=list(map(int,sys.stdin.readline().rstrip().split(' ')))
monitor_a=0
monitor_b=0
entire=(N*2)+(M*2)

if(monitor[0]==1):
    monitor_a=0
elif(monitor[0]==2):
    monitor_a=M
elif(monitor[0]==3):
    monitor_b=0
else:
    monitor_b=N

if(monitor[0]==3 or monitor[0]==4):
    monitor_a=monitor[1]
else:
    monitor_b=monitor[1]

for a,b in store:
    a_idx=0
    b_idx=0

    if(a==1):
        a_idx=0
    elif(a==2):
        a_idx=M
    elif(a==3):
        b_idx=0
    else:
        b_idx=N

    if((a==3 or a==4)):
        a_idx=b
    else:
        b_idx=b

    if(abs(monitor_a-a_idx)==M):
        tmp=M+b_idx+monitor_b
    elif(abs(monitor_b-b_idx)==N):
        tmp=N+a_idx+monitor_a
    elif(monitor_a==a_idx):
        tmp=abs(monitor_b-b_idx)
    elif(monitor_b==b_idx):
        tmp=abs(a_idx-monitor_a)
    else:
        tmp=abs(monitor_a-a_idx)+abs(monitor_b-b_idx)

    answer+=min(tmp,entire-tmp)

print(answer)