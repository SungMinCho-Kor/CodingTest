import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

if a.isnumeric():
    answer = int(a) + 3
elif b.isnumeric():
    answer = int(b) + 2
elif c.isnumeric():
    answer = int(c) + 1

if answer % 15 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)