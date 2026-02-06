import sys
from collections import defaultdict

input=sys.stdin.readline

N,M,K=map(int,input().split())
fireball=defaultdict(list)

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
velocity=[[0,2,4,6],[1,3,5,7]]

answer=0

for i in range(M):
    r,c,m,s,d=map(int,input().split()) # x,y,질량,속력,방향
    fireball[(r-1,c-1)].append([m,d,s]) # 질량,방향,속력

for i in range(K):
    tmp=defaultdict(list) # 이동한 결과

    #이동
    for key,value in fireball.items():
        x,y=key
        for m,d,s in value:
            n_x=(x+(dx[d]*s))%N
            n_y=(y+(dy[d]*s))%N

            tmp[(n_x,n_y)].append([m,d,s])

    #가공
    for key,value in tmp.items():
        m_sum=0
        s_sum=0
        even_n=0
        odd_n=0
        n_v=0

        if(len(value)>1):
            for m,d,s in value:
                m_sum+=m
                s_sum+=s
                if(d%2==0):
                    even_n+=1
                else:
                    odd_n+=1

            if(even_n==len(value) or odd_n==len(value)):
                n_v=0
            else:
                n_v=1

            n_s=s_sum//len(value)
            tmp[key]=[]

            if(m_sum//5>0):
                for j in range(4):
                    tmp[key].append([m_sum//5,velocity[n_v][j],n_s])

    fireball=tmp

for key,value in fireball.items():
    for m,d,s in value:
        answer+=m

print(answer)