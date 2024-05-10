n,m=map(int,input().split())
array=[]
for _ in range(n): 
    array.append(list(map(int,input().split())))
dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]
x,y=0,0
temp=[[0]*m for _ in range(n)]
result=0

#바이러스가 사방으로 퍼지는 경우
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx <n and 0 <= ny < m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)
#현재 맵에서 안전영역의 크기 계산
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

#울타리를 설치하면서 매번 안전영역의 크기 계산
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=array[i][j]
        #바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        #안정영역 최대값 계산
        result=max(result,get_score())
        return
    #빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                array[i][j]=1
                count+=1
                dfs(count)
                array[i][j]=0
                count-=1
dfs(0)
print(result)

