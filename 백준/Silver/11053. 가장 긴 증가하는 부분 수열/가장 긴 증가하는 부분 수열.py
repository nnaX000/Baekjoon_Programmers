num=int(input())
array=list(map(int,input().split(' ')))
case=[0].append(array)
dp=[0]*(num+1)
for i in range(len(array)):
    maxx=0
    temp=array[i]
    for j in range(0,i):
        if(temp>array[j]):
            if(maxx<=dp[j]):
                maxx=dp[j]
    dp[i]=maxx+1
print(max(dp))