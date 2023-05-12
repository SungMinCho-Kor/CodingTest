
def sosoo(n):
    cnt = 0
    if n<2:
        return False
    elif n==2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True
    
def permutation(base, array):
    if base:
        s.add(int(base))
    for i, j in enumerate(array):
        permutation(base + j, array[:i] + array[i+1:])
    
s = set()
def solution(numbers):
    answer = 0
    permutation("",list(numbers))
    print(s)
    for i in s:
        if sosoo(i):
            print(i)
            answer+=1
    return answer