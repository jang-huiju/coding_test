from collections import Counter
T=int(input())
for test_case in range(1,T+1):
    test=int(input())
    score=list(map(int,input().split()))
    max_firtst=Counter(score).most_common()[0][0]
    print('#{} {}'.format(test,max_firtst))
