import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
lans = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

start = 1
end = max(lans)

while start <= end:
    count = 0
    mid = (start + end) // 2
    for lan in lans:
        count += lan // mid
    if count >= N:
        start = mid + 1
    elif count < N:
        end = mid - 1
print(end)