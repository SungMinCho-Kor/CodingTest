import sys
input = sys.stdin.readline

sn = int(input())
switch = list(map(int, input().split()))
n = int(input())

def toggle(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0

for _ in range(n):
    gender, k = map(int, input().split())
    if gender == 1:
        for i in range(k-1, sn, k):
            toggle(i)
    else:
        i = 1
        k -= 1
        toggle(k)
        while k - i >=0 and k + i < sn:
            if switch[k-i] == switch[k+i]:
                toggle(k-i)
                toggle(k+i)
            else:
                break
            i += 1

for i in range(sn):
    print(switch[i], end = ' ')
    if (i + 1)%20 == 0:
        print()