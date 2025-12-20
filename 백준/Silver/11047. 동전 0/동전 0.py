import sys

N,K=map(int,sys.stdin.readline().rstrip().split(' '))

coin=[]
for i in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.sort(reverse=True)
idx=0

answer=0

while(K!=0):
    if(K>=coin[idx]):
        answer+=K//coin[idx]
        K%=coin[idx]
    idx+=1

print(answer)