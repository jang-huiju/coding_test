T=int(input())
for test_case in range(1,T+1):
    n,k=map(int,input().split())
    array=[] #1은 들어갈수있는 자리 0은 들어갈수없음
    count=0 #총합
    for _ in range(n):
        array.append(list(map(int,input().split())))
    for i in range(n):
        row_cnt=0
        column_cnt=0
        for j in range(n):
            #가로 검사
            if array[i][j]==1:
                row_cnt+=1
            if array[i][j]==0  or j==(n-1):
                if row_cnt==k:
                    count+=1
                row_cnt=0

            #세로 검사
            if array[j][i]==1:
                column_cnt+=1
            if array[j][i]==0 or j==(n-1):
                if column_cnt==k:
                    count+=1
                column_cnt=0
    print('#{} {}'.format(test_case,count))
                
    