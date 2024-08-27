import sys

input = sys.stdin.readline
P = int(input())

for _ in range(P):
    students = list(map(int, input().split()))
    T = students.pop(0)
    row = []
    answer = 0
    for i in range(20):
        student = students[i]
        k = len(row)
        for j in range(len(row)):
            if row[j] > student:
                k = j
                break
        answer += len(row) - k
        row.insert(k, student)
    print(T, answer)