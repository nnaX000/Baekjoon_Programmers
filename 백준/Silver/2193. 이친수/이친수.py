N=int(input())

array=[[0,1],[1,0]]

for i in range(2,N):
    array.append([sum(array[i-1]),array[i-1][0]])

print(sum(array[N-1]))