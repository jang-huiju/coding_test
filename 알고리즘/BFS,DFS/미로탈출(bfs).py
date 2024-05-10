from collections import deque
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[0,0,1,-1] #좌우하상
dy=[-1,1,0,0]
def bfs(x,y):
    q=deque([(x,y)])
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[a][b]+1
                q.append((nx,ny))
    return graph[n-1][m-1]
    
start_x,start_y=1,1

print(bfs(start_x-1,start_y-1))

        
            


