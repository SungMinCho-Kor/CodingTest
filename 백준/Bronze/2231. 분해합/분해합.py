def solution(n):
    for i in range(1,n):
        lst = list(str(i))
        summ = i
        for j in lst:
            summ+= int(j)
        if summ == n:
            return i
    return 0

print(solution(int(input())))