T=int(input())
for test_case in range(1,T+1):
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    start_m,start_d,final_m,final_d=map(int,input().split())
    sum=0
    #시작달-마지막달사이의 기간
    if start_m==final_m:
        sum+=final_d-start_d+1
    else:
        for i in range(start_m,final_m):
            sum+=days[i]
        sum+=final_d-start_d+1
        
    print(f'#{test_case} {sum}')