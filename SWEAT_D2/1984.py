T=int(input())
for test_case in range(1,T+1):
    num=list(map(int,input().split()))
    min_value=min(num)
    max_value=max(num)
    sum=0
    for n in num:
        if min_value==n or max_value==n:
            continue
        sum+=n
    print(sum/(len(num)-2))