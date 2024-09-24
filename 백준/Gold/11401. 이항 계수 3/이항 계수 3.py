import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000000007

def get_factorial(n):
    res = 1
    for i in range(2, n+1):
        res = (res*i) % p
    return res

def get_pow(n, k):
    if k == 1:
        return n%p
    half_pow = get_pow(n, k//2)%p
    if k % 2 == 0:
        return half_pow * half_pow % p
    else:
        return half_pow * half_pow * n % p

first = get_factorial(n)
second = get_factorial(k) * get_factorial(n-k)
print(first * get_pow(second, p-2) % p)