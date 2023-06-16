def solution(msg):
    answer = []
    dic = []
    dic.append('')
    for k in range(26):
        dic.append(chr((ord('A') + k)))
    k = 28
    i = 0
    while i < len(msg):
        string = ""+msg[i]
        i += 1
        while string in dic and i<len(msg):
            string += msg[i]
            i+=1
        if string not in dic:
            answer.append(dic.index(string[:-1]))
            dic.append(string)
        else:
            answer.append(dic.index(string))     
            break
        i-=1
    return answer