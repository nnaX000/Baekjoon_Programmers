import sys

N,L,R,X=map(int,sys.stdin.readline().split(' '))
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
answer=set()

def dfs(start,path):
    global answer
    aligned_path=sorted(path)

    if(len(aligned_path)>=2 and tuple(aligned_path) not in answer):
        max_value=-1
        min_value=10000001
        sum_value=0

        for i in aligned_path:
            sum_value+=A[i]
            if(A[i]<min_value):
                min_value=A[i]
            if(A[i]>max_value):
                max_value=A[i]
        
        if(L<=sum_value<=R and max_value-min_value>=X):
            answer.add(tuple(aligned_path))

    for i in range(start,N):
        aligned_path.append(i)
        new_path=aligned_path[:]
        dfs(i+1, new_path)
        aligned_path.pop()

dfs(0,[])

print(len(answer))