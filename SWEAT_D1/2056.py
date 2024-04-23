t=int(input())
days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for test in range(1,t+1):
    num=input()
    year=num[0:4]
    month=num[4:6]
    day=num[6:]
    if  0<int(month)<13 and 0<int(day)<=days[int(month)]:
        print("#"+str(test)+" "+year+"/"+month+"/"+day)
    else:
        print("#"+str(test)+" -1")