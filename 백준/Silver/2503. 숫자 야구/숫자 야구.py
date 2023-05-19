from itertools import permutations

nums = sorted(list(permutations([1,2,3,4,5,6,7,8,9],3)))
n = int(input())
strings = [input() for _ in range(n)]
ans_cnt = 0
for i in nums:
    num = ""
    for j in i:
        num+=str(j)
    flag = 0
    for j in strings:
        wnum,ws,wb = map(int, j.split())
        wnum = str(wnum)
        s=0
        b=0
        for k in range(3):
            if num[k]==wnum[k]:
                s+=1
            elif num[k] in wnum:
                b+=1
        if ws != s or wb != b:
            flag = 1
    if flag==0:
        ans_cnt+=1
print(ans_cnt)