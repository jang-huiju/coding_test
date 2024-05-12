T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    data=[[0]*n for _ in range(n)]
    direction=0 #오른쪽 방향
    dx=[0,1,0,-1] #동남서북
    dy=[1,0,-1,0]
    count=1
    x,y=0,0 #시작위치

    while count<=n*n:
        if 0<=x<n and 0<=y<n and data[x][y]==0:
            data[x][y]=count
            count+=1
        else:
            x-=dx[direction]
            y-=dy[direction]
            direction=(direction+1) % 4
            
        x+=dx[direction]
        y+=dy[direction]


    print('#'+str(test_case))
    for i in data:
        print(*i)