n=int(input())
sum=0

while True:
    if n<1:
        break
    sum+=n%10
    n=n//10
print(sum)

    