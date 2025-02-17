'''
1: 12345
2: 21232425 21232425
3: 3311224455 3311224455
'''
def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    as1 = 0
    as2 = 0
    as3 = 0
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            as1 += 1
        if answers[i] == s2[i%8]:
            as2 += 1
        if answers[i] == s3[i%10]:
            as3 += 1
    if as1 >= as2 and as1 >= as3:
        answer.append(1)
    if as2 >= as1 and as2 >= as3:
        answer.append(2)
    if as3 >= as2 and as3 >= as1:
        answer.append(3)
    return answer