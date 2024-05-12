T=int(input())

for test_case in range(1,T+1):
    #A사 1리터당 P원, 
    #B사 기본요금Q R리터이하인 경우 기본요금 초과량 1리터당 S원
    P, Q, R, S, W = map(int,input().split())
    test1=0
    test2=0
    test1=W*P
    if W<=R:
        test2=Q
    else:
        test2=Q+(W-R)*S
    result=1e9
    result=min(test1,test2)
    print(f'#{test_case} {result}')

