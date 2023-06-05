
'''
4 7
3 0 1 4 3 1 2
OOOXOOO
XOOXXOO
XOOXXOX
XOXXXXX
-------
'''
import sys
input = sys.stdin.readline
h,w = map(int,input().split())
block_num = list(map(int,input().split()))
block = []
for i in range(h-1,-1,-1):#현재 높이:i
    tmp = ""
    for j in range(w):
        if i<block_num[j]:
            tmp+='X'
        else:
            tmp+='O'
    block.append(tmp)

answer = 0
for i in range(h):
    for j in range(1,w-1):
        if block[i][j] == 'O' and 'X' in block[i][:j] and 'X' in block[i][j+1:]:
            answer+=1

# for i in range(h):
#     print(block[i])
print(answer)
    