import sys

input=sys.stdin.readline

N=int(input())
M=int(input())
S=input()

answer=0

i=0
cnt=0

while(i<len(S)-1):
    if(S[i-1]=="I" and S[i]=="O" and S[i+1]=="I"):
        cnt+=1
        if(cnt>=N):
            answer+=1
        i+=2
    else:
        cnt=0
        i+=1

print(answer)