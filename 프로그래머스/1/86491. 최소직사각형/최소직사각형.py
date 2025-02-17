'''
가로  세로
60   50
30   70

'''
def solution(sizes):
    answer_w, answer_h = 0, 0
    for w, h in sizes:
        w1 = max(answer_w, w)
        h1 = max(answer_h, h)
        
        w2 = max(answer_w, h)
        h2 = max(answer_h, w)
        if w1*h1 > w2*h2:
            answer_w = w2
            answer_h = h2
        else:
            answer_w = w1
            answer_h = h1
            
    return answer_w * answer_h