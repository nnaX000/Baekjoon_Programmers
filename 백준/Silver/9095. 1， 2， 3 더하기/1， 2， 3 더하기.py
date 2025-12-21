import sys

T=int(sys.stdin.readline().rstrip())
count=0

def dfs(n):
    global count

    if(n==0):
        count+=1

    if(n-1>=0):
        dfs(n-1)
    
    if(n-2>=0):
        dfs(n-2)

    if(n-3>=0):
        dfs(n-3)

for i in range(T):
    tmp=int(sys.stdin.readline().rstrip())
    count=0

    dfs(tmp)

    print(count)