from collections import deque 
n,l,r=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]

#특정위치에서 출발하여 모든 연합을 체크한뒤에 데이터 갱신
def process(x,y,index):
    #(x,y)의 위치와 연결된 나라정보를 담는 리스트
    united=[]
    united.append((x,y))
    q=deque()
    q.append((x,y))
    union[x][y]=index #현재연합의 번호할당
    summary=data[x][y] #현재연합의 전체인구수
    count=1 #현재연합의 국가수
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(data[nx][ny]-data[x][y])<=r:
                    q.append((nx,ny))
                    union[nx][ny]=index
                    summary+=data[nx][ny]
                    count+=1
                    united.append((nx,ny))
    for i,j in united:
        data[i][j]=summary//count
    return count
total_count=0
while True:
    union=[[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i,j,index)
                index+=1
    if index==n*n:
        break
    total_count+=1
print(total_count)
