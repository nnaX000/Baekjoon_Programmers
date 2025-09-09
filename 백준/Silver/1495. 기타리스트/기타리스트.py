import sys

N,S,M=map(int,sys.stdin.readline().rstrip().split(' ')) # 곡 개수, 시작볼륨, 최대 볼륨
V=list(map(int,sys.stdin.readline().rstrip().split(' ')))

#[5,3,7]
#[(-,+)] 시작볼륨 : 5 최대볼륨 : 10
#[(0,10),(7,3),(0,10)]
dp=[set() for i in range(N+1)]
dp[0].add(S)
check=False

for i in range(1,N+1):
   for j in dp[i-1]:
      plus=j+V[i-1]
      minus=j-V[i-1]

      plus_in=(True if 0<=plus<=M else False)
      minus_in=(True if 0<=minus<=M else False)

      if(plus_in):
         dp[i].add(plus)
    
      if(minus_in):
         dp[i].add(minus)

   if (len(dp[i])==0):
        check=True
        print(-1)
        break
   
if(not check):
   print(max(dp[N]))