T=int(input())
for test_case in range(1,T+1):
    n,k=map(int,input().split())
    total_list=[]
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for _ in range(n):
        mid,final,hws=map(int,input().split())
        total = (mid * 0.35) + (final * 0.45) + (hws*0.2)
        total_list.append(total)

    k_score=total_list[k-1]
    total_list.sort(reverse=True)
    div=n//10
    final_k_score=total_list.index(k_score)//div
    print('#{} {}'.format(test_case, grades[final_k_score]))



