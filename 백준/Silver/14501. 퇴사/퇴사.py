N=int(input())

counseling=[]
income=[0]*(N+1)

for i in range(N):
    temp=list(map(int,input().split(' ')))
    counseling.append(temp)

for i in range(N-1,-1,-1):
    if(i+counseling[i][0]<=N):
        income[i]=max(counseling[i][1]+income[i+counseling[i][0]],income[i+1])
    else:
        income[i]=income[i+1]

print(income[0])