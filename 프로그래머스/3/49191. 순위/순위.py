'''
내가 이길 사람 수 + 나한테 질 사람 수 == n - 1
내가 이길 사람 수 :  
'''

from collections import deque

def solution(n, results):
    answer = 0
    
    l_graph = [[] for _ in range(n + 1)]
    w_graph = [[] for _ in range(n + 1)]
    
    for a, b in results:
        l_graph[a].append(b)
        w_graph[b].append(a)
        
    # 이길 사람 수 계산
    for i in range(1, n+1):
        l_visit = [False for _ in range(n+1)]
        queue = deque([i])
        while queue:
            p = queue.popleft()
            for loser in l_graph[p]:
                if l_visit[loser] == False:
                    l_visit[loser] = True
                    queue.append(loser)
        loser_count = l_visit.count(True)
        
        w_visit = [False for _ in range(n+1)]
        queue = deque([i])
        while queue:
            p = queue.popleft()
            for loser in w_graph[p]:
                if w_visit[loser] == False:
                    w_visit[loser] = True
                    queue.append(loser)
        winner_count = w_visit.count(True)
        
        if loser_count + winner_count == n-1:
            answer += 1
    
    return answer