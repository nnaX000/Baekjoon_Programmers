import sys

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
S=sys.stdin.readline().rstrip()

stand="IOI"+("OI")*(N-1)
answer=0

for i in range(len(S)-len(stand)+1):
    if(S[i:i+len(stand)]==stand):
        answer+=1

print(answer)