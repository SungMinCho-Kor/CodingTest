import sys

input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0

total = 0
answer = 0
while True:
    if total >= s:
        if answer == 0 or answer > right - left :
            answer = right - left
        total -= array[left]
        left += 1
    elif right>=n:
        break
    elif total < s:
        total += array[right]
        right += 1
print(answer)