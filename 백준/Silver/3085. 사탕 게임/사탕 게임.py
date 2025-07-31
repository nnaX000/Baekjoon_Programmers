import sys

N=int(sys.stdin.readline().rstrip())

result_1=0
result_2=0
result=0
candy=[]

for i in range(N):
    candy.append(list(sys.stdin.readline().rstrip()))

def check(candy):
    max_value=0
    for i in range(N):
        count=1
        prev=candy[i][0]
        for j in range(1,N):
            if(prev==candy[i][j]):
                count+=1
            else:
                if(count>max_value):
                    max_value=count
                prev=candy[i][j]
                count=1

        if(count>max_value):
            max_value=count

    for i in range(N):
        count=1
        prev=candy[0][i]
        for j in range(1,N):
            if(prev==candy[j][i]):
                count+=1
            else:
                if(count>max_value):
                    max_value=count
                prev=candy[j][i]
                count=1

        if(count>max_value):
            max_value=count

    return max_value
    

for i in range(N):
    for j in range(N):
        if(j+1<N and candy[i][j]!=candy[i][j+1]):
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]

            result_1=check(candy)

            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]

        if(i+1<N and candy[i][j]!=candy[i+1][j]):
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]

            result_2=check(candy)

            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]

        result=max(result,result_1,result_2)

print(result)