class Solution {
    public int[] solution(String[] park, String[] routes) {
        // 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
        // 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
        // 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
        // N은 북쪽, S는 남쪽, W는 서쪽, E는 동쪽
        int H=park.length;
        int W=park[0].length();
        
        int x=0;
        int y=0;
        
        int[] answer = new int[2];
        
        for (int i = 0 ; i<park.length ; i++){
            for (int j = 0 ; j<park[i].length() ; j++){
                if(park[i].charAt(j)=='S'){
                    x=i;
                    y=j;
                    break;
                }
            }
        }
    
        
        for (int i = 0 ; i<routes.length ; i++){
            String[] parts = routes[i].split(" ");
            String direction = parts[0];
            int num = Integer.parseInt(parts[1]);
        
            
            if(direction.equals("E")){
                for (int j = 0 ; j<num ; j++){
                    y+=1;
                    if(y>=W || park[x].charAt(y)=='X'){
                        for (int k = 0 ; k<=j ; k++){
                            y-=1;
                        }
                        break;
                    }
                }
            }else if(direction.equals("W")){
                for (int j = 0 ; j<num ; j++){
                    y-=1;
                    if(y<0 || park[x].charAt(y)=='X'){
                        for (int k = 0 ; k<=j ; k++){
                            y+=1;
                        }
                        break;
                    }
                }
            }else if(direction.equals("S")){
                for (int j = 0 ; j<num ; j++){
                    x+=1;
                    if(x>=H || park[x].charAt(y)=='X'){
                        for (int k = 0 ; k<=j ; k++){
                            x-=1;
                        }
                        break;
                    }
                }
            }else{
                for (int j = 0 ; j<num ; j++){
                    x-=1;
                    if(x<0 || park[x].charAt(y)=='X'){
                        for (int k = 0 ; k<=j ; k++){
                            x+=1;
                        }
                        break;
                    }
                }
            }
        }
        
        answer[0]=x;
        answer[1]=y;
        
        return answer;
    }
}