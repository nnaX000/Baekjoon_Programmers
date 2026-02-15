import sys

input=sys.stdin.readline

N,K=map(int,input().split())
answer=float('-inf')

N_list=[]
for i in str(N):
    N_list.append(i)

case=[]
candi=[i for i in range(len(N_list))]

visited=set()

#조합
def dfs(start,arr):
    if(len(arr)==2):
        case.append(arr[:])
        return
    
    for i in range(start,len(candi)):
        arr.append(candi[i])
        dfs(i+1,arr)
        arr.pop()
    
dfs(0,[])

#시뮬레이션
def op(sv,count):
    global answer
    global visited

    if(count==K):
        answer=max(answer,int(''.join(sv)))
        return
    
    for i in range(len(case)):
        first,second=case[i][0],case[i][1]

        if(first==0 and sv[second]=="0"):
            continue
        
        sv[first],sv[second]=sv[second],sv[first]

        if(tuple([tuple(sv),count+1]) not in visited):
            op(sv,count+1)
            visited.add(tuple([tuple(sv),count+1]))

        sv[first],sv[second]=sv[second],sv[first]

op(N_list,0)

if(answer==float('-inf')):
    print(-1)
else:
    print(answer)