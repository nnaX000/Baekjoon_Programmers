import sys
from collections import defaultdict

input=sys.stdin.readline

C=int(input())

# 모든 문자는 ‘.’(앉을 수 있는 자리) 또는 ‘x’(앉을 수 없는 자리, 소문자)로 구성된다.

dx=[-1,-1,-1,0]
dy=[-1,0,1,-1]

def pop_count(x):
    return x.bit_count()

for i in range(C):
    N,M=map(int,input().split()) 
    classroom=[list(input().rstrip()) for _ in range(N)]
    unavailable=[]
    case=[]
    answer=float('-inf')
    
    # 앉을 수 없는 자리 만들기
    for k in range(N):
        tmp=0
        for c in range(M):
            if(classroom[k][c]=="x"):
                tmp|=(1<<c)
        unavailable.append(tmp)

    #만들 수 있는 자리 모두 만들기
    for k in range(1<<M):
        if(k&(k<<1)==0):
            case.append(k)

    pre=defaultdict(int)
    pre[0]=0

    for k in range(N):
        cur=defaultdict(int)
        for key,value in pre.items():
            for c in case:
                cnt=pop_count(c)
                #x 있는 칸에 사람 놓으려 하는 경우는 제외
                if(c&unavailable[k]!=0):
                    continue

                #왼쪽 대각선에 겹치는거 없는지 확인
                if(c&(key<<1)!=0):
                    continue

                #오른쪽 대각선에 겹치는거 없나 확인
                if(c&(key>>1)!=0):
                    continue

                cv=cnt+value
                cur[c]=max(cur[c],cv)

        pre=cur

    for key,value in pre.items():
        answer=max(value,answer)

    print(answer)