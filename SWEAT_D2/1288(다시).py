T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    array=[0]*10
    count=0

    while (0 in array):
        str_n=str(n)
        for i in str_n:
            array[int(i)]+=1
        count+=1
        n=count*int(str_n)
    print('#{} {}'.format(test_case,count*n))


