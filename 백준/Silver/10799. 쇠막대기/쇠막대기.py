'''
아이디어 잡기

(를 만나면 레이저의 (인지 막대기의 (인지 알 수 없다
)를 처음 만나면 레이저의 )이고, ) 직후의 )는 막대기의 )이다
flag를 사용하여 판단

'''

import sys

elements = list(sys.stdin.readline().rstrip())

count = 0
total = 0
flag = False
for element in elements:
    if element == '(':
        count += 1
        flag = False
    elif element == ')':
        if flag: #막대기 )
            count -= 1
            total += 1
        else: # lazor )
            count -= 1
            total += count
            flag = True
print(total)