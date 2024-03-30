T = int(input())
for test_case in range(1, T + 1):
    sum=0
    data=list(map(int,input().split()))   
    for j in data:
        if  j%2!=0:
            sum+=j
    print("#"+str(test_case)+" "+str(sum))