
'''

'''

from itertools import product
def solution(word):
    
    dictionary = []
    for i in range(1, 6):
        for element in list(product(["A", "E", "I", "O", "U"], repeat = i)):
            tmp = ""
            for c in element:
                tmp += c
            dictionary.append(tmp)
    dictionary.sort()
    return dictionary.index(word) + 1