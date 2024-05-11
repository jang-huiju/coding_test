T=int(input())
for test_case in range(1,T+1):
    sdoku=[]
    for _ in range(9):
        sdoku.append(list(map(int,input().split())))
    def check_sdoku():
        for i in range(9):
            row_num=[0]*10
            column_num=[0]*10
            for j in range(9):
                row=sdoku[i][j]
                column=sdoku[j][i]
                if row_num[row]: return 0
                if column_num[column]: return 0
                row_num[row]=1
                column_num[column]=1
            if i%3==0 and j%3==0:
                temp=[0]*10
                for k in range(i,3+i):
                    for s in range(j,j+3):
                        if temp[data[k][s]]:
                            return 0
                        temp[k][s]=1
        return 1
    result=0
    result=check_sdoku()
    print('#{} {}'.format(test_case,result))
