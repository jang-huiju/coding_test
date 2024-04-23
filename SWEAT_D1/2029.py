t=int(input())

for test in range(1,t+1):
    a,b=map(int,input().split())
    print("#"+str(test)+" "+str(a//b)+" "+str(a%b))