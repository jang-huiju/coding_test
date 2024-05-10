n=int(input())
x,y=1,1
plans=input().split()
dx=[0,0,-1,1] #좌우상하 x좌표
dy=[-1,1,0,0] #좌우상하 y좌표
move_types=['L','R','U','D']
for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny <1 or nx>n or ny>n:
        continue
    x,y=nx,ny
print(x,y)