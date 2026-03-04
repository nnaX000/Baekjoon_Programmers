def solution(arr):
    answer = -1
    n=len(arr)//2+1 #숫자 개수 - 4
    maxdp=[[float('-inf') for _ in range(n)] for _ in range(n)]
    mindp=[[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(0,len(arr),2):
        maxdp[i//2][i//2]=int(arr[i])
        mindp[i//2][i//2]=int(arr[i])
        
    for L in range(2,n+1): #범위
        for i in range(n-L+1): # 시작 시점 - 0
            j=i+L-1 #끝 시점 - 1
            
            for k in range(i,j):
                op=arr[k*2+1]
                
                if(op=="+"):
                    cal_min=mindp[i][k]+mindp[k+1][j]
                    cal_max=maxdp[i][k]+maxdp[k+1][j]
                else:
                    cal_min=mindp[i][k]-maxdp[k+1][j]
                    cal_max=maxdp[i][k]-mindp[k+1][j]
                    
                maxdp[i][j]=max(maxdp[i][j],cal_max)
                mindp[i][j]=min(mindp[i][j],cal_min)
            
    return maxdp[0][n-1]