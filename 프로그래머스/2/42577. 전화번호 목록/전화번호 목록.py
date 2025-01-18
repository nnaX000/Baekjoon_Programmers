def solution(phone_book):
    keep=True
    answer = True
    book={}
    for j in phone_book:
        book[j]=0
    for i in phone_book:
        tmp=""
        for j in i:
            tmp+=j
            if(tmp in book and tmp!=i):
                answer=False
                keep=False
                break
        if(not keep):
            break
    return answer