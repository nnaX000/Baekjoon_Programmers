import sys

# M번만 통장에서 돈 빼서 쓰기
# 모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원 인출

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
costs=[]

for i in range(N):
    costs.append(int(sys.stdin.readline().rstrip()))

start=1
end=100000000000000
wallet=0
answer=float('inf')

while(start<=end):
    middle=(start+end)//2
    count=M
    wallet=0
    check=False

    for i in range(N):
        if(wallet<costs[i] and count>0):
            if(middle<costs[i]):
                check=True
                start=middle+1
                break
            else:
                count-=1
                wallet=middle-costs[i]
        elif(wallet<costs[i] and count==0):
            check=True
            start=middle+1
            break
        elif(wallet>=costs[i]):
            wallet-=costs[i]

    if(not check):
        end=middle-1
        answer=min(answer,middle)

print(answer)