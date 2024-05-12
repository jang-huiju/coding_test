T=int(input())
for test_case in range(1,T+1):
    
    n,m=map(int,input().split())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    result=0
    array=[]
    #swap
    if len(num1)>len(num2):
        num1,num2=num2,num1
    for i in range(len(num2)-len(num1)+1):
        for j in range(n):
            result+=(num1[j]*num2[i+j])
        array.append(result)
    print(f'#{test_case} {max(array)}')

   
