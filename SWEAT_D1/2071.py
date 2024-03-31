T = int(input())

for test_case in range(1, T + 1):
    sum=0
    n=list(map(int,input().split()))
    for i in n:
        sum+=i
    avg=round(sum/10)
    print("#"+str(test_case)+" "+str(avg))