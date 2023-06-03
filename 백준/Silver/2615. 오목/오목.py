import sys

board = [list(map(int,sys.stdin.readline().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if j<15:#가로로 5개
            ls1 = board[i][j:j+5]
            if ls1 == [1,1,1,1,1] or ls1 == [2,2,2,2,2]:# 5목일 가능성이 있음. 6목인지 확인필요
                if 0<=j-1<19 and 0<=j+5<19:
                    if board[i][j-1] != ls1[0] and board[i][j+5] !=ls1[0]:
                        print(ls1[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=j-1<19:
                    if board[i][j-1] != ls1[0]:
                        print(ls1[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=j+5<19:
                    if board[i][j+5] !=ls1[0]:
                        print(ls1[0])
                        print(i+1,j+1)
                        sys.exit()
                else:
                    print(ls1[0])
                    print(i+1,j+1)
                    sys.exit()
        if i<15:#세로로 5개
            ls2 = [board[i+k][j] for k in range(5)]
            if ls2==[1,1,1,1,1] or ls2 == [2,2,2,2,2]:#5목 가능, 6목 확인 ㄱㄱ
                if 0<=i-1<19 and 0<=i+5<19:
                    if board[i-1][j] != ls2[0] and board[i+5][j] != ls2[0]:
                        print(ls2[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i-1<19:
                    if board[i-1][j] != ls2[0]:
                        print(ls2[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i+5<19:
                    if board[i+5][j] != ls2[0]:
                        print(ls2[0])
                        print(i+1,j+1)
                        sys.exit()
                else:
                    print(ls2[0])
                    print(i+1,j+1)
                    sys.exit()
        if i>3 and j<15:#우상향 대각선
            ls3 = [board[i-k][j+k] for k in range(5)]
            if ls3==[1,1,1,1,1] or ls3 == [2,2,2,2,2]:
                if 0<=i+1<19 and 0<=j-1<19 and 0<=i-5<19 and 0<=j+5<19:#양측 다 검사해야함
                    if board[i+1][j-1] != ls3[0] and board[i-5][j+5] != ls3[0]:#5목임
                        print(ls3[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i+1<19 and 0<=j-1<19:
                    if board[i+1][j-1] != ls3[0]:#5목임
                        print(ls3[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i-5<19 and 0<=j+5<19:
                    if board[i-5][j+5] != ls3[0]:#5목임
                        print(ls3[0])
                        print(i+1,j+1)
                        sys.exit()
                else:
                    print(ls3[0])
                    print(i+1,j+1)
                    sys.exit()
                    
        if i<15 and j<15:#우하향 대각선
            ls4 = [board[i+k][j+k] for k in range(5)]
            if ls4==[1,1,1,1,1] or ls4 == [2,2,2,2,2]:
                if 0<=i-1<19 and 0<=j-1<19 and 0<=i+5<19 and 0<=j+5<19:
                    if board[i-1][j-1] != ls4[0] and board[i+5][j+5] != ls4[0]:
                        print(ls4[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i-1<19 and 0<=j-1<19:
                    if board[i-1][j-1] != ls4[0]:
                        print(ls4[0])
                        print(i+1,j+1)
                        sys.exit()
                elif 0<=i+5<19 and 0<=j+5<19:
                    if board[i+5][j+5] != ls4[0]:
                        print(ls4[0])
                        print(i+1,j+1)
                        sys.exit()
                else:
                    print(ls4[0])
                    print(i+1,j+1)
                    sys.exit()
print(0)
        