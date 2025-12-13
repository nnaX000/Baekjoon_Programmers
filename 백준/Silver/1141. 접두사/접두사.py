import sys

N=int(sys.stdin.readline().rstrip())
words=[sys.stdin.readline().rstrip() for i in range(N)]
words.sort(key=lambda x:-len(x))
answer=[words[0]]

for i in range(1,N):
    check=False
    for j in range(len(answer)):
        if(answer[j].startswith(words[i])):
            check=True
            break
    if(not check):
        answer.append(words[i])

print(len(answer))