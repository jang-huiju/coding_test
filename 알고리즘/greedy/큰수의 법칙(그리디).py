n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
first=data[-1]
second=data[-2]
result=0
#1번째 풀이
# cnt=0
# for i in range(m):
#     if cnt==k:
#         result+=second
#         cnt=0
#     else:
#         result+=first
#         cnt+=1
# print(result)

#2번째 풀이
cnt=m//(k+1)*k
cnt+=m%(k+1)
result+=cnt*first
result+=(m-cnt)*second
print(result)
