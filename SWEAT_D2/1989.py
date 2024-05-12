T=int(input())
for test_case in range(1,T+1):
    n=input()
    if n[::-1]==n:
        print(1)
    else:
        print(0)
    
    
