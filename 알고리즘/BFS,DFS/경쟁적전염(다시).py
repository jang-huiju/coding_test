from collections import deque
n,k=map(int,input().split())
virus=[] #바이러스위치
data=[] #맵정보
s,target_x,target_y=map(int,input().split())
for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        if data[i][j]!=0:
            virus.append((data[i][j],0,i,j))
dx=[-1,0,1,0]
dy=[0,-1,0,1] #상좌하우
virus.sort()
q=deque(virus)
while q:
    kind,time,x,y=q.popleft()
    if time==s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and data[nx][ny]==0:
            data[nx][ny]=data[x][y]
            q.append((data[nx][ny],time+1,nx,ny))
print(data[target_x-1][target_y-1])
