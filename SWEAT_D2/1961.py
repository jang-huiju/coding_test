#주의사항 
#90도는 n,i,j를 활용하여 규칙찾기
#180도는 거꾸로규칙
#270도는 90도와 비슷한 규칙이용
#join 문법은 문자열에 적용
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    array=[]
    for _ in range(n):
        array.append(list(map(int,input().split())))
    def rotation(arr):
        new_array=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_array[i][j]=arr[n-j-1][i]
        return new_array
    array_90=rotation(array)
    array_180=rotation(array_90)
    array_270=rotation(array_180)
    print(f'#{test_case}')
    for x,y,z in zip(array_90,array_180,array_270):
        print(f"{''.join(map(str,x))} {''.join(map(str,y))} {''.join(map(str,z))}")
#-----------
#2번째 풀이
# T=int(input())
# for test_case in range(1,T+1):
#     n=int(input())
#     array=[]
#     for _ in range(n):
#         array.append(list(map(int,input().split())))
#     array_90=[[0]*n for _ in range(n)]
#     array_180=[[0]*n for _ in range(n)]
#     array_270=[[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             array_90[i][j]=array[n-j-1][i]
#             array_180[i][j]=array[n-i-1][n-j-1]
#             array_270[i][j]=array[j][n-i-1]
#     print(f'#{test_case}')
#     for x,y,z in zip(array_90,array_180,array_270):
#         print(f"{''.join(map(str,x))} {''.join(map(str,y))} {''.join((map(str,z)))}")


                

    