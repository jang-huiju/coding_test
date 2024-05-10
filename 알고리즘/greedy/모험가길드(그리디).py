n=int(input())
person=list(map(int,input().split()))
person.sort()
result=0 # 총그룹수
cnt=0 #현재그룹 인원수
for i in person:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0
print(result)