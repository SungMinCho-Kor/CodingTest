import sys

input = sys.stdin.readline

a, b = input().split()
min_a = ""
max_a = ""
for c in a:
    if c == '5':
        max_a += '6'
    else:
        max_a += c
    if c == '6':
        min_a += '5'
    else:
        min_a += c
min_b = ""
max_b = ""
for c in b:
    if c == '5':
        max_b += '6'
    else:
        max_b += c
    if c == '6':
        min_b += '5'
    else:
        min_b += c
print(int(min_a) + int(min_b), int(max_a) + int(max_b))