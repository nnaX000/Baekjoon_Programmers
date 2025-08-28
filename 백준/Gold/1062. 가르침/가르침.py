import sys

N,K=map(int,sys.stdin.readline().rstrip().split(' '))
words=[sys.stdin.readline().rstrip() for i in range(N)]
alpha=["a","n","t","i","c"]
max_value=0

def dfs(candi,start):
    global max_value

    if(len(candi)==K or len(candi)==len(alpha)):
        num=0
        for i in words:
            check=False
            for j in range(4,len(i)):
                if(i[j] not in candi):
                    check=True
                    break
            if(not check):
                num+=1
        max_value=max(max_value,num)
        return

    for i in range(start,len(alpha)):
        candi.add(alpha[i])
        dfs(candi,i+1)
        candi.remove(alpha[i])


if(K<5):
    print(0)
else:
    for i in words:
        for j in range(4,len(i)-4):
            if(i[j] not in alpha):
                alpha.append(i[j])

    dfs(set(["a","n","t","i","c"]),5)
    print(max_value)