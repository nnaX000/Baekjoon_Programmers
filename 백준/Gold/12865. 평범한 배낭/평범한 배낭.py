num,weight=map(int,input().split(' '))
array=[]
for i in range(num):
    tmp=list(map(int,input().split(' ')))
    array.append(tmp)
array=sorted(array,key=lambda x:x[0])

dp=[0]*(weight+1)
for n,v in array:
     for i in range(weight,n-1,-1):
        dp[i]=max(dp[i],dp[i-n]+v)
print(max(dp))