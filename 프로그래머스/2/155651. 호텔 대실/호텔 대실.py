import heapq

def solution(book_time):
    book_time.sort(key = lambda x:x[0])
    answer = 0
    end=[]
    heap = [i[:] for i in book_time]
    heapq.heapify(heap)
    
    while(heap):
        start,finish = heapq.heappop(heap)
        sh,sm = map(int,start.split(":"))
        fh,fm = map(int,finish.split(":"))
        
        if(end):
            now_h = end[0][0]
            now_m = end[0][1]+10
            if(now_m>=60):
                now_h+=1
                now_m-=60
            
            if(now_h<sh): #아예 시가 빠른 경우 - 그 방 드가기
                end[0][0] = fh
                end[0][1] = fm
            elif(now_h==sh): #시는 같음
                if(now_m<=sm): #분이 빠름 - 그 방 드가기
                    end[0][0] = fh
                    end[0][1] = fm
                else: #분이 느림 - 그 방 못들어감. 새 방 드가기
                    answer+=1
                    end.append([fh,fm])
            else: #아예 시부터 빠름 - 새 방 드가기
                answer+=1
                end.append([fh,fm])
        else:
            end.append([fh,fm])
            answer+=1
            
        end.sort()
            
    return answer