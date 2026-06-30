n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

between=A & B

answer=0

for i in A:
    if(i not in between):
        answer+=1

for i in B:
    if(i not in between):
        answer+=1

print(answer)