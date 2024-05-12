T=int(input())
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    array=[]
    max_value=0
    for i in range(n):
        array.append(list(map(int,input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            result=0
            for k in range(m):
                for l in range(m):
                    result+=array[i+k][j+l]
            max_value=max(result,max_value)
    print('#{} {}'.format(test_case,max_value))

    

       



