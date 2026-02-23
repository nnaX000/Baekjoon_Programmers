import sys
import bisect

input=sys.stdin.readline

N=int(input())

meetings=[]
end=[]

for i in range(N):
    meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x:x[1])

for a,b,c in meetings:
    end.append(b)

dp=[0,meetings[0][2]]

for i in range(1,N):
    #나는 처음에 가장 시작시간보다 일찍 끝나는 회의를 for문으로 찾으려 했는데 bisect로 찾으면 됐었다..
    pos=bisect.bisect_right(end,meetings[i][0],0,i)

    #해당 회의를 선택할수도 있고 안하고 그냥 바로 전 회의 끌고와서 쓸수도 있음..
    dp.append(max(dp[i],dp[pos]+meetings[i][2]))

print(max(dp))