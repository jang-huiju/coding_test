T=int(input())
for test_case in range(1,T+1):
    num=str(test_case)
    count=0
    for i in num:
        if '3' in i or '6' in i or '9' in i:
            count+=1
    if count>0:
        print('-'*count,end='')
    else:
        print(num,end='')
    print('',end=' ')
