import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    answer=""
    num,word=sys.stdin.readline().rstrip().split(' ')

    for j in word:
        answer+=j*int(num)
    
    print(answer)