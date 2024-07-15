import sys

num = int(sys.stdin.readline().strip())

answers = []

for i in range(666, 10000000):
    tmp = str(i)
    if '666' in tmp:
        answers.append(i)

print(answers[num-1])