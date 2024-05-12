T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    day=list(map(int,input().split()))
    profit=0
    last=day[-1]
    for i in range(n-1,-1,-1):
        if last>day[i]:
            profit+=(last-day[i])
        else:
            last=day[i]
    print('#{} {}'.format(test_case,profit))