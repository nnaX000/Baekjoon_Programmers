def solution(number, k):
    stack=[]
    for i in number:
        while(k>0 and stack and i>stack[-1]):
            stack.pop()
            k-=1
        stack.append(i)
    answer=''.join(stack[:len(number)-k])
    return answer