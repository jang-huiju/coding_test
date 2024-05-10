num=input()
count_1=0 #1로 바꾸는 경우
count_0=0 #0으로 바꾸는 경우
if num[0]=='1':
    count_0+=1
else:
    count_1+=1
for i in range(len(num)-1):
    if num[i]!=num[i+1]:
        if num[i+1]=='1':
            count_0+=1
        else:
            count_1+=1

print(min(count_0,count_1))

