import sys

#중복순열
#순열->visited

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,M=map(int,input().split())
N_array=list(map(int,input().split()))
N_array.sort()

array=[]

def dfs(start):

    if(len(array)==M):
        print(*array)
        return

    used=set()
    for i in range(start,N):
        if(N_array[i] not in used):
            array.append(N_array[i])
            used.add(N_array[i])
            dfs(i)
            array.pop()

dfs(0)