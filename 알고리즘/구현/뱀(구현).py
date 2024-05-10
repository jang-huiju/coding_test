n=int(input()) #보드크기
k=int(input()) #사과갯수
#맵정보초기화
d=[[0]*(n+1) for _ in range(n+1)]
#맵정보갱신(사과있는위치 1로 표시)
for _ in range(k):
    a,b=map(int,input().split())
    d[a][b]=1
#방향회전정보입력
info=[]
l=int(input())
for _ in range(l):
    x,c=input().split()
    info.append((int(x),c))
#동남서북 위치정보
direction=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
# 회전 함수 정의
def turn(direction,c):
    if c=='L':
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction
# 뱀의 머리 위치
x,y=1,1
# 뱀이 존재하는 위치는 2로 표시 
d[x][y]=2 
# 다음에 회전할 정보
index=0
result=0
# 뱀이 차지하고 있는 정보
q=[(x,y)]
#시뮬레이션 시작
while True:
    nx=x+dx[direction]
    ny=y+dy[direction]
    print('{} {} {}'.format(nx,ny,result))
    #맵범위안에 있고 뱀의 몸통이 없는 위치
    if 1<= nx and nx<=n and 1<=ny and ny<=n and d[nx][ny]!=2:
        #사과가 없다면 이동후에 꼬리제거
        if d[nx][ny]==0:
            d[nx][ny]=2
            q.append((nx,ny))
            px,py=q.pop(0)
            d[px][py]=0
        # 사과가 있다면 이동후 꼬리 그대로 두기
        if d[nx][ny]==1:
            d[nx][ny]=2
            q.append((nx,ny))
    #벽이나 뱀의 몸통과 부딪히면
    else:
        result+=1
        break
    result+=1
    x=nx
    y=ny    
    #회전 할 시간인 경우 회전
    if index<l and result==info[index][0]:
        direction=turn(direction,info[index][1])
        index+=1
print(result)


