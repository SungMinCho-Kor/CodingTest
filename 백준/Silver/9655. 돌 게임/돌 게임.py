import sys

def function(N):
    if ((N%6)%4)%2 > 0:
        return "SK"
    else:
        return "CY"

N = int(sys.stdin.readline().rstrip())

print(function(N))