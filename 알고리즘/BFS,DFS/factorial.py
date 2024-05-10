#반복적구현
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

#재귀함수
def factorial2(n):
    result2=1
    if n<=1:
        return 1
    return n*factorial2(n-1)
    n-=1
print(factorial(5))
print(factorial2(5))
