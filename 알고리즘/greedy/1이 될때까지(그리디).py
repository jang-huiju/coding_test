#1번째 풀이
n,k=map(int,input().split())
# count=0
# while k <=n:
#     if n%k==0:
#         n/=k
#         count+=1
#     else:
#         n-=1
#         count+=1
# while 1<n:
#     n-=1
#     count+=1
# print(count)
#2번째 풀이
target=0
count=0
while True:
    target=(n//k)*k
    count+=(n-target)
    n=target
    if n<k:
        break
    n//=k
    count+=1
count+=(n-1)
print(count)

