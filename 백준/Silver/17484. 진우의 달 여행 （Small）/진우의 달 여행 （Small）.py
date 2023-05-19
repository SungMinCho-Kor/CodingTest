

answer = set()
def func(i,j,way,n,m,space,score):
    score += space[i][j]
    if i==n-1:
        answer.add(score)
        return
        
    
    if way != 1 and j>0:
        func(i+1,j-1,1, n,m,space,score)
    if way != 2:
        func(i+1,j,2,n,m,space,score)
    if way != 3 and j<m-1:
        func(i+1,j+1,3,n,m,space,score)
    
            

def solution(n,m,space):
    for i in range(m):
        if i!=0:
            func(0,i,1,n,m,space,0)
        func(0,i,2,n,m,space,0)
        if i!= m-1:
            func(0,i,3,n,m,space,0)
        
    print(min(answer))
n,m = map(int,input().split())

space = [list(map(int,input().split())) for _ in range(n)]
# print(space)
solution(n,m,space)
# print(solution(n,m,space))
        