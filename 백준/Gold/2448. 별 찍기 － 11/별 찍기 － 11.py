import sys

input=sys.stdin.readline

N=int(input())

arr=[[' ' for _ in range((N//3)*5+((N//3)-1))] for _ in range(N)]

def draw(x, y, size): #size=높이
    if size == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = '*'
        arr[x+1][y+1] = '*'
        for i in range(-2, 3): # 맨 아래 점 다섯개
            arr[x+2][y+i] = '*'
    else:
        half = size // 2
        draw(x, y, half)
        draw(x + half, y - half, half) # 왼쪽
        draw(x + half, y + half, half) # 오른쪽

draw(0, N-1, N)

for i in arr:
    print("".join(i))