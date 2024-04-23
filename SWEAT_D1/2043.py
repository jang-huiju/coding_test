p,k=map(int,input().split())

#1번째 풀이
# print(abs(p-k)+1)

#2번째 풀이
# result=0
# for i in range(k,p+1):
#     result+=1
#     k+=1
# print(result)

#3번째 풀이
result=0
while(True):
    result+=1
    if p==k:
        break
    k+=1
print(result)