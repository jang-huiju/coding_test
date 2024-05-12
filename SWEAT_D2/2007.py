T=int(input())
for test_case in range(1,T+1):
    data=input()
    for i in range(1,len(data)):
        if data[:i]==data[i:i+i]:
            s=data[:i]
            break
    print('#{} {}'.format(test_case,len(s)))

        

