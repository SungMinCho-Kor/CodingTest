def solution(n,m,board):
    boards = []
    for i in range(n-7):
        for j in range(m-7):
            tmp = [board[i+k][j:j+8] for k in range(8)]
            boards.append(tmp)
    answer = n*m
    for i in boards:
        cnt1 = 0
        cnt2 = 0
        for p in range(8):
            for q in range(8):
                if (p+q)%2 == 0 and i[p][q] == 'W':
                    cnt1+=1
                elif (p+q)%2 == 1 and i[p][q] == 'B':
                    cnt1+=1
                if (p+q)%2 == 0 and i[p][q] == 'B':
                    cnt2+=1
                elif (p+q)%2 == 1 and i[p][q] == 'W':
                    cnt2+=1
        answer = min(cnt1,cnt2,answer)
    
    return answer
    
    
    
    
n,m = map(int,input().split())
board = [input() for _ in range(n)]
print(solution(n,m,board))