T = int(input())

for test_case in range(1, T + 1):
    sdoku=[]
    for _ in range(9):
        sdoku.append(list(map(int,input().split())))
    #중복 있을때 0 없을때 1
    def check_sdoku():
        for i in range(9):
            row_num=[0]*10
            column_num=[0]*10
            for j in range(9):
                #가로검사
                row=sdoku[i][j]
                #세로검사
                column=sdoku[j][i]

                #중복된 숫자가 있을때
                if row_num[row]==1: return 0
                if column_num[column]==1: return 0
				
                row_num[row]=1
                column_num[column]=1

                #3x3행렬일때 중복검사
                if i%3==0 and j%3==0:
                    temp=[0]*10
                    for k in range(i,3+i):
                        for s in range(j,3+j):
                            num=sdoku[k][s]
                            if temp[num]==1:
                                return 0
                            temp[num]=1
        return 1
    check=check_sdoku()
    print('#{} {}'.format(test_case,check))
    
