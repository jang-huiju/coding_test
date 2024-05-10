n=input()
result=int(n[0])
for i in range(1,len(n)):
    data=int(n[i])
    if data<=1 or result<=1:
        result+=data
    else:
        result*=data
print(result)
