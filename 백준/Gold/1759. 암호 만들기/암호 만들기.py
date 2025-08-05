import sys

L,C=map(int,sys.stdin.readline().rstrip().split(' '))
char=list(set(sys.stdin.readline().rstrip().split(' ')))
char.sort()

def dfs(start,tmp):
    if(len(tmp)==L):
        mo=0
        for i in tmp:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                mo+=1
        if(mo>0 and L-mo>1):
            print(''.join(tmp))
            return
    
    for i in range(start+1,len(char)):
        tmp.append(char[i])
        dfs(i,tmp)
        tmp.pop()

tmp=[]
dfs(-1,tmp)