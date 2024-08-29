import sys
input = sys.stdin.readline

board = [list(map(int, list(input().rstrip()))) for _ in range(9)]

def get_candidates(i, j):
    exclude_set = set()
    exclude_set.update(board[i])
    exclude_set.update([board[k][j] for k in range(9)])
    for p in range((i//3) * 3, (i//3) * 3 + 3):
        for q in range((j//3) * 3, (j//3) * 3 + 3):
            exclude_set.add(board[p][q])
    return {1,2,3,4,5,6,7,8,9} - exclude_set


def dfs(s_i, s_j):
    s_j += 1
    while s_i<9:
        while s_j<9:
            if board[s_i][s_j] == 0:
                candidates = get_candidates(s_i, s_j)
                if not candidates:
                    return
                for candidate in candidates:
                    board[s_i][s_j] = candidate
                    dfs(s_i, s_j)
                board[s_i][s_j] = 0
                return
            s_j +=1
        s_j = 0
        s_i += 1
    
    if s_i >= 9:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        exit(0)

dfs(0, -1)