'''
가장 짧은 변환 과정 찾아 -> BFS

begin 에서 시작 -> begin을 queue에 넣기, visit

begin에서 바뀔 수 있는 놈들 words에서 다 찾아.

'''

from collections import deque

n = 0

def check(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            cnt+=1
    if cnt == 1:
        return True
    return False

def bfs(begin,target,words, visit):
    queue = deque()
    queue.append(begin)
    cnt = 0
    global n
    while queue:
        word = queue.popleft()
        if word in words:
            n = visit[words.index(word)]
        for i in range(len(words)):
            if visit[i] == 0 and check(word,words[i]):
                queue.append(words[i])
                visit[i] = n+1
                if words[i] == target:
                    return visit[i]
                
                
                
def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for _ in range(len(words))]
    return bfs(begin,target,words, visit)