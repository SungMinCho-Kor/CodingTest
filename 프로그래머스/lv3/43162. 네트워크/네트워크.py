'''
[
    [1, 0, 0, 1], 
    [0, 1, 0, 0], 
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]

1.
0 visit -> 0,1 0,2 0,3 ... 들어가다가 
    visit도 0이고 computers도 1이면 dfs 시작

'''

visit = []

def dfs(computers, j):
    for i in range(len(computers[0])):
        if visit[j][i] == 0 and computers[j][i] == 1:
            visit[j][i] = 1
            dfs(computers, i)
        
    

def solution(n, computers):
    answer = 0
    global visit
    visit = [[0 for _ in range(len(computers[0]))] for _ in range(len(computers))]
    print(visit)
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1 and visit[i][j] == 0:
                answer+=1
                visit[i][j] = 1
                dfs(computers,j)
    return answer