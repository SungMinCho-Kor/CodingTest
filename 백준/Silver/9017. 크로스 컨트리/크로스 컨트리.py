'''
- 6명인지 확인
- 4등까지만 점수
- 점수가 똑같다면 index 비교

'''

class Team:
    def __init__(self):
        self.total_score = 0
        self.fifth_index = 0
        self.member_count = 0

import sys

def remover(rank):
    team_set = set(rank)
    for team in team_set:
        if rank.count(team) != 6:
            while team in rank:
                rank.remove(team)
    return rank
    

def function(N, rank):
    real_rank = remover(rank)
    rank_set = set(real_rank)
    teams = {}
    for r in rank_set:
        teams[r] = Team()
    score = 1
    for r in real_rank:
        if teams[r].member_count == 4:
            teams[r].fifth_index = score
            teams[r].member_count += 1
        if teams[r].member_count < 4:
            teams[r].member_count += 1
            teams[r].total_score += score
        score += 1
    answer = []
    for r in rank_set:
        answer.append([teams[r].total_score, teams[r].fifth_index, teams[r].member_count, r])
    answer.sort(key=lambda x: (x[0], x[1]))
    print(answer[0][-1])
    
    
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    rank = list(map(int, sys.stdin.readline().rstrip().split()))
    function(N, rank)

