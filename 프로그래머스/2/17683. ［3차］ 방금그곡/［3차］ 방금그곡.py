from collections import defaultdict

def solution(m, musicinfos):
    answer = ''
    candi = []
    music = defaultdict(list)
    
    m=m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "C").replace("E#", "F")
    
    #일단 재생되는 노래대로 저장
    for i in range(len(musicinfos)):
        start,end,name,record = musicinfos[i].split(",")
        start_hour,start_mn = map(int,start.split(":"))
        end_hour,end_mn = map(int,end.split(":"))
        tmp=""
        
        time = (end_hour-start_hour)*60 + (end_mn - start_mn)
        repeat = (time//len(record)) 
        ram = time % len(record)
        
        record = record.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "C").replace("E#", "F")
        
        repeat = (time // len(record))
        ram = time % len(record)
        tmp = record * repeat + record[:ram]
                
        music[name] = [tmp,time,i]
    
    #일치하는 노래
    for key,value in music.items():
        if(m in value[0]):
            candi.append([key,value[1],value[2]])
    
    candi.sort(key=lambda x: (-x[1], x[2]))
    
    if(len(candi)==0):
        return "(None)"
    else:
        answer = candi[0][0]
    
    return answer