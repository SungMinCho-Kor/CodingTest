import sys

input = sys.stdin.readline
king_str, stone_str, n = input().rstrip().split()
n = int(n)
king_i = 7 - (int(king_str[1]) - 1)
king_j = ord(king_str[0]) - ord('A')
stone_i = 7 - (int(stone_str[1]) - 1)
stone_j = ord(stone_str[0]) - ord('A')

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
operator = {
    'R' : 0,
    'L' : 1,
    'B' : 2,
    'T' : 3,
    'RT' : 4,
    'LT' : 5,
    'RB' : 6,
    'LB' : 7
}

for _ in range(n):
    k = operator[input().rstrip()]
    nk_i = king_i+dx[k]
    nk_j = king_j+dy[k]
    if 0<=nk_i<8 and 0<=nk_j<8:
        if (nk_i, nk_j) == (stone_i, stone_j):
            ns_i = stone_i + dx[k]
            ns_j = stone_j + dy[k]
            if 0<=ns_i<8 and 0<=ns_j<8:
                king_i = nk_i
                king_j = nk_j
                stone_i = ns_i
                stone_j = ns_j
        else:
            king_i = nk_i
            king_j = nk_j
print(chr(ord('A') + king_j) + str(8 - king_i))
print(chr(ord('A') + stone_j) + str(8 - stone_i))