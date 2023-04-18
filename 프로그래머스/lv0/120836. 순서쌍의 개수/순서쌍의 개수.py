def solution(n):
    cnt = 0
    for i in range(1,int(n**(0.5)) + 1):
        if n%i == 0:
            cnt+=1
    return cnt*2 - 1 if int(n**(0.5))==n**(0.5) else cnt*2