import itertools

def sosoo(n):
    cnt = 0
    print(int(n**0.5))
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True
    
    
def solution(numbers):
    answer = 0
    ls = list(numbers)
    s = set()
    for i in range(1,len(numbers) + 1):
        tmp = list(itertools.permutations(ls,i))
        for j in tmp:
            j = int("".join(j))
            if j ==1 or j == 0:
                continue
            s.add(j)
    print(s)
    for i in s:
        if sosoo(i):
            answer+=1
    return answer