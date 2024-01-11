
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().rstrip().split())

boxes = []

queue = deque()

for i in range(H):
    box = []
    for j in range(N):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(M):
            if line[k] == 1:
                queue.append([i, j, k])
            
        box.append(line)
    boxes.append(box)
    
while queue:
    i, j, k = queue.popleft()
    close = [
        [i + 1, j, k], 
        [i, j + 1, k], [i, j - 1, k], [i, j, k + 1], [i, j, k - 1], 
        [i - 1, j, k]
        ]
    for point in close:
        x, y, z = point
        if 0<=x<H and 0<=y<N and 0<=z<M and boxes[x][y][z] == 0:
            queue.append(point)
            boxes[x][y][z] = boxes[i][j][k] + 1
            
def check():
    max_value = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 0:
                    return 0
                max_value = max(max_value, boxes[i][j][k])
    return max_value
    
print(check() - 1)

        
        
        
        
        
        
        
        