import sys

N = int(sys.stdin.readline().rstrip())
sizes = list(map(int,sys.stdin.readline().rstrip().split()))
T, P = map(int,sys.stdin.readline().rstrip().split())

t_count = 0
for size in sizes:
    if size % T > 0:
        t_count += size//T + 1
    else:
        t_count += size//T
print(t_count)
print(N//P, N%P)