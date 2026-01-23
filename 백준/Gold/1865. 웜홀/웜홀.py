import sys
import heapq

input=sys.stdin.readline

#한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지

def bf():
    T = [0] * (N+1)

    for i in range(N):
        for route in roads:
            a,b,c=route

            if(T[b]>T[a]+c):
                T[b]=T[a]+c

                if(i==N-1):
                    return "YES"
    
    return "NO"


TC=int(input())

for i in range(TC):
    N,M,W=map(int,input().split()) # 지점 수, 도로 개수, 웜 홀 개수

    answer=[[] for _ in range(N+1)]
    result=[]
    check=False

    roads=[]
    for j in range(M):
        a,b,c=map(int,input().split()) # 연결된 지점번호1, 연결된 지점번호2, 걸리는 시간
        roads.append([a,b,c])
        roads.append([b,a,c])
    
    for j in range(W):
        S,E,T=map(int,input().split()) # 시작 지점, 도착 지점, 줄어드는 시간

        roads.append([S,E,-T])

    print(bf())