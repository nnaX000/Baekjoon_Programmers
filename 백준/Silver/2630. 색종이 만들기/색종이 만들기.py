import sys

input=sys.stdin.readline

N=int(input())

paper=[list(map(int,input().rstrip().split())) for _ in range(N)]
length=len(paper)

sum_value=[0,0]

visited=set()

stand=length

while(stand>=1):
    for i in range(0,length,stand): # x시작점 잡아줌
        for j in range(0,length,stand): # y시작점 잡아줌
            check=False
            s=0
            tmp_visited=set()
            for k in range(i,i+stand):
                for l in range(j,j+stand):
                    if((k,l) not in visited):
                        if(k==i and l==j):
                            s=paper[k][l]
                            tmp_visited.add((k,l))
                        elif(paper[k][l]!=s):
                            check=True
                            break
                        elif(paper[k][l]==s):
                            tmp_visited.add((k,l))
                    else:
                        check=True
                        break
                
                if(check):
                    break

            if(not check):
                if(s==0):
                    sum_value[0]+=1
                else:
                    sum_value[1]+=1

                visited=visited.union(tmp_visited)
            
    stand//=2

print(sum_value[0],sum_value[1])