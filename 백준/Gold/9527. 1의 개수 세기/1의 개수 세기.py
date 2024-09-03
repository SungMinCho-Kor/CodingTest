import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def count_bi(num):
    bi = bin(num)
    answer = 0
    front_one = 0
    for i in range(2, len(bi)):
        binary = int(bi[i])
        if binary == 1:
            k = len(bi) - i - 1
            answer += int(k * (2**(k-1)) + 1) + front_one*(2 ** k)
            front_one += 1
    return answer
print(count_bi(b) - count_bi(a-1))