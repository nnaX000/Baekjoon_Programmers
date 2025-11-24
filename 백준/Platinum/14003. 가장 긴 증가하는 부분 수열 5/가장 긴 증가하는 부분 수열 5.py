import sys
import bisect

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
L=[A[0]] # 최장수열 길이
L_idx=[1] #각 요소별로 L에 들어가는 인덱스 저장

for i in range(1,N):
    if(L[-1]<A[i]):
        L.append(A[i])
        L_idx.append(len(L))
    else:
        tmp=bisect.bisect_left(L,A[i])
        L[tmp]=A[i]
        L_idx.append(tmp+1)

max_value=max(L_idx)
answer=[]

for i in range(len(L_idx)-1,-1,-1):
    if(L_idx[i]==max_value):
        answer.append(A[i])
        max_value-=1

answer.reverse()
print(len(L))
print(*answer)