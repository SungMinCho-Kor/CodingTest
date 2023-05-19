
answer = set()

def check(n,board):
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt+=1
            else:
                answer.add(cnt)
                cnt = 1
        answer.add(cnt)
        cnt=1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                cnt+=1
            else:
                answer.add(cnt)
                cnt = 1
        answer.add(cnt)
                

def solution(n, board):
    for i in range(n):
        for j in range(n):
            if j+1 < n and board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                check(n, board)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if i+1 < n and board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                check(n, board)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    return max(answer)




n = int(input())
board = [list(input()) for _ in range(n)]
# print(board)
print(solution(n,board))
        