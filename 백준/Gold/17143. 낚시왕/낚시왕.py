import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

water = [[False for _ in range(C)] for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d-1 == 0 or d-1 == 1:
        s %= (R-1)*2
    else:
        s %= (C-1)*2
    water[r-1][c-1] = (s, d-1, z)

answer = 0
for c in range(C): # 낚시왕 위치 j
    # print("--water--")
    # for line in water:
    #     print(*line)
    for r in range(R): # 상어 위치 검사
        if water[r][c]: # 상어 잡기
            s, d, z = water[r][c]
            answer += z
            water[r][c] = False
            # print("--")
            # print(r,c,s,d,z)
            
            break
    
    # 상어 이동
    new_water = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if water[i][j]:
                s, d, z = water[i][j]
                ti, tj = i, j
                # s 만큼 이동
                for _ in range(s):
                    if d == 0 or d == 1:
                        ti += dx[d]
                        if ti < 0:
                            ti = 1
                            if d == 0:
                                d = 1
                            else:
                                d = 0
                        elif ti >= R:
                            ti = R-2
                            if d == 0:
                                d = 1
                            else:
                                d = 0
                    else:
                        tj += dy[d]
                        if tj < 0:
                            tj = 1
                            if d == 2:
                                d = 3
                            else:
                                d = 2
                        elif tj >= C:
                            tj = C-2
                            if d == 2:
                                d = 3
                            else:
                                d = 2
                
                # 상어 놓기
                if new_water[ti][tj]:
                    ns, nd, nz = new_water[ti][tj]
                    if nz < z:
                        new_water[ti][tj] = (s, d, z)
                else:
                    new_water[ti][tj] = (s, d, z)
    water = new_water
print(answer)