T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    data=[[0]*n for _ in range(n)]
    print('#'+str(test_case))
    for i in range(n):
        for j in range(i+1):
            if j==0 or i==j:
                data[i][j]=1
            else:
                data[i][j]=data[i-1][j-1]+data[i-1][j]
            print(data[i][j],end=' ')
        print()

            
