import sys

input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for _ in range(n)]

numbers.sort()

number_list = []
for i in range(n-1):
    number_list.append(numbers[i+1] - numbers[i])
number_list.sort()

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

k = number_list[0]
for i in range(1, n-1):
    k = gcd(number_list[i], k)
answer = []
for i in range(1, int(k**0.5) + 1):
    if k % i == 0:
        answer.append(i)
        if int(i**2) != k:
            answer.append(k//i)
answer.sort()
print(*answer[1:])