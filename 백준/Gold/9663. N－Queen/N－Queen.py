'''

n을 입력받아 n개의 수의 permutations를 출력하기

5
OXOOO
OOOOO
OOOOX
OOOOO
OOOOO

i,j
0,1
2,4
i==i or j==j or abs(i-i)/abs(j-j) == 1 : 안되는 거임
'''
import sys

n = int(sys.stdin.readline())
cnt = 0
def dfs(i,ls):
    global cnt
    if i==n:
        cnt+=1
        return
    for j in range(n):
        flag = 0
        for l in ls:
            if l[0]==i or l[1]==j or abs(i-l[0]) / abs(j-l[1]) == 1:
                flag = 1
                break
        if flag == 0:
            dfs(i+1,ls+[[i,j]])
dfs(0,[])
print(cnt)