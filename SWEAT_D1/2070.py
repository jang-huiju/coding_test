T = int(input())

for test_case in range(1, T + 1):

        n,k=map(int,input().split())
        if n<k:
            print("#"+str(test_case)+" <")
        elif n==k:
            print("#"+str(test_case)+" =")
        else:
            print("#"+str(test_case)+" >")
  
