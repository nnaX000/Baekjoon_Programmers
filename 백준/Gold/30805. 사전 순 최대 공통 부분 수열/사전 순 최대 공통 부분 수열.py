import sys

input=sys.stdin.readline

answer=[]

N=int(input())
A=list(map(int,input().split()))

M=int(input())
B=list(map(int,input().split()))

result=set(A) & set(B)

if(len(result)==0):
    print(0)
    sys.exit(0)
    
start=max(set(A) & set(B))
answer.append(start)

a_idx=0
b_idx=0

for i in range(len(A)):
    if(A[i]==start):
        a_idx=i
        break

for i in range(len(B)):
    if(B[i]==start):
        b_idx=i
        break

a_candi=A[a_idx+1:]
b_candi=B[b_idx+1:]

while(a_candi and b_candi):
    a_c=set(a_candi)
    b_c=set(b_candi)

    result=a_c & b_c

    if(len(result)>0):
        stand=max(result)
        answer.append(stand)

        for i in range(len(a_candi)):
            if(a_candi[i]==stand):
                a_idx=i
                break

        for i in range(len(b_candi)):
            if(b_candi[i]==stand):
                b_idx=i
                break

        a_candi=a_candi[a_idx+1:]
        b_candi=b_candi[b_idx+1:]  

    else:
        break

print(len(answer))
print(*answer)   