def solution(s):
    ls = list(map(int, s.split()))
    answer = '' + str(min(ls)) + ' ' + str(max(ls))
    return answer