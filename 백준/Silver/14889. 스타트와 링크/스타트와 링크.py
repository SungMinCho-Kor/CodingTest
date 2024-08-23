import sys
input = sys.stdin.readline

n = int(input())
members = [i for i in range(n)]
scores = [list(map(int, input().split())) for _ in range(n)]


visit = [False for _ in range(n)]

answer = 20 * 20 * 100

def calc_score(team):
    global answer
    team2 = []
    for member in members:
        if member not in team:
            team2.append(member)
    team1_score = 0
    team2_score = 0
    for i in range(n//2 - 1):
        for j in range(i + 1, n//2):
            team1_score += scores[team[i]][team[j]] + scores[team[j]][team[i]]
            team2_score += scores[team2[i]][team2[j]] + scores[team2[j]][team2[i]]
    answer = min(answer, abs(team1_score - team2_score))
    
def dfs(team, visit, start):
    if len(team) == n//2:
        calc_score(team)
        return
    
    for i in range(start + 1, n):
        if visit[i] == False:
            visit[i] = True
            dfs(team + [i], visit, i)
            visit[i] = False
    
dfs([], visit, -1)
print(answer)