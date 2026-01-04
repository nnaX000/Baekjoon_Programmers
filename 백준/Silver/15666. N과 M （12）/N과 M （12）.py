import sys

#중복순열
#순열->visited

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,M=map(int,input().split())
N_array=list(map(int,input().split()))
N_array.sort()
answer=set()

def dfs(array):
    global answer

    if(len(array)==M):
        check=False

        for i in range(1,M):
            if(array[i-1]>array[i]):
                check=True
                break

        if(not check):
            answer.add(tuple(array[:]))

        return

    for i in range(N):
        array.append(N_array[i])
        dfs(array)
        array.pop()

dfs([])

answer=list(answer)
answer.sort()

for i in answer:
    print(*i)