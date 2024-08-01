import sys

while True:
    string = sys.stdin.readline().rstrip()
    string = string.lower()
    if string == "#":
        break
    answer = 0
    for c in "aeiou":
        answer += string.count(c)
    print(answer)