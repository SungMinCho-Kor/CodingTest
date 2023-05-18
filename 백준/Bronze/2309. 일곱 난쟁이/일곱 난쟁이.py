def solution(lst):
    for i in range(len(lst) - 1):
        for j in range(i+1,len(lst)):
            tmp = lst[:i]+lst[i+1:j] + lst[j+1:]
            if sum(tmp) == 100:
                tmp.sort()
                return tmp
    return 0

for i in solution([int(input()) for _ in range(9)]):
    print(i)