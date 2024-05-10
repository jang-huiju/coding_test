from itertools import combinations
#배열 크기
n=int(input())
#복도의 정보
board=[]
#선생님의 위치정보
teachers=[]
#빈공간의 위치 정보
spaces=[]
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j]=='T':
            teachers.append((i,j))
        if board[i][j]=='X':
            spaces.append((i,j))

direction=0 #위쪽방향
#감시되는지 안되는지 확인하는 함수(발견 T 미발견 F)
def watch(x,y,direction):
    #위쪽
    if direction==0:
        while x>=0:
            if board[x][y]=='S':
                return True
            else:
                return False
            x-=1
    #아래쪽
    if direction==1:
        while x<n:
            if board[x][y]=='S':
                return True
            else:
                return False
            x+=1
    #왼쪽
    if direction==2:
        while y>=0:
            if board[x][y]=='S':
                return True
            else:
                return False
            y-=1
    #오른쪽
    if direction==3:
        while y<n:
            if board[x][y]=='S':
                return True
            else:
                return False
            y+=1
    return False
#장애물설치이후 감지되는 지 확인 여부(감지 T 감지x F)
def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
            else:
                return False 
find=False #학생이 한명이라도 감지되지않도록 설치 할수 있는 지의 여부

for data in combinations(spaces,3):
    print(data)
    for x,y in data:
        board[x][y]='O'
    if not process():
        find=True
        break
    for x,y in data:
        board[x][y]='X'

if find:
    print("yes")
else:
    print("No")






            


            

