a,b=map(int,input().split())
# 1번째방법 풀이 
# if (a-b)==1 or (b-a)==2:
#     print("A")
# else:
#     print("B")

#2번째 방법 풀이
if a%b==1:
    print("A")
else:
    print("B")
