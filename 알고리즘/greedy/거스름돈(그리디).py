money=[500,100,50,10]
cnt=0
n=int(input())
for i in money:
    cnt+=n//i
    n%=i
print(cnt)
