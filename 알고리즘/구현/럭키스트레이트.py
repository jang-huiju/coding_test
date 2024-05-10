n=input()
l_result=0
r_result=0
for i in range(len(n)):
    if len(n)/2<i+1:
        r_result+=int(n[i])
    else:
        l_result+=int(n[i])
if l_result==r_result:
    print("LUCKY")
else:
    print("READY")