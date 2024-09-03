import sys

input = sys.stdin.readline
n, m = map(int, input().split())

n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

n_arr.extend(m_arr)
n_arr.sort()
print(*n_arr)