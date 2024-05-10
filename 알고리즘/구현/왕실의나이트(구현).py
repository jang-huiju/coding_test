steps=[(1,2),(-1,-2),(-1,2),(1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
result=0 #경우의 수
n=input()
column=ord(n[0])-ord('a')+1 #행
row=int(n[1]) #열


for step in steps:
    n_row=row+step[0]
    n_column=column+step[1]
    if 0<n_row<=8 and 0<n_column<=8:
        result+=1
print(result)