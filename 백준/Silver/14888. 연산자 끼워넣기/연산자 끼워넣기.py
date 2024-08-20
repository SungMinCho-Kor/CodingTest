import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_val = 1e10
max_val = -1e10

def dfs(res, cnt, plus, minus, multiply, divide):
    global min_val
    global max_val
    
    if cnt == n:
        min_val = min(min_val, res)
        max_val = max(max_val, res)
        return
    
    if plus > 0:
        dfs(res + numbers[cnt], cnt + 1, plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(res - numbers[cnt], cnt + 1, plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(res * numbers[cnt], cnt + 1, plus, minus, multiply-1, divide)
    if divide > 0:
        if res < 0:
            dfs(-((-res)//numbers[cnt]), cnt + 1, plus, minus, multiply, divide-1)
        else:
            dfs(res // numbers[cnt], cnt + 1, plus, minus, multiply, divide-1)

dfs(numbers[0], 1, plus, minus, multiply, divide)
print(max_val)
print(min_val)
