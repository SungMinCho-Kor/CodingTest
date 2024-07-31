import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
friends = graph[1]
friends_friends = set()
for friend in friends:
    friends_friends = friends_friends.union(set(graph[friend]))
answer_set = friends_friends.union(set(friends))
if 1 in answer_set:
    answer_set.remove(1)
print(len(answer_set))