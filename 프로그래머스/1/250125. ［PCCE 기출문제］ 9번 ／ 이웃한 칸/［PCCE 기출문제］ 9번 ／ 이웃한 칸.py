def solution(board, h, w):
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    count = 0
    n = len(board)
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < n and 0 <= nw < n and board[nh][nw] == board[h][w]:
            count += 1
    
    return count