import sys

input = sys.stdin.readline

n = int(input())

fb = [0, 1]

for i in range(n - 1):
    fb.append(fb[i] + fb[i + 1])
print(fb[-1])