n=input()
sum=0
result=[]
for i in n:
    if i.isalpha():
        result.append(i)
    else:
        sum+=int(i)
result.sort()
print(''.join(result)+str(sum))
