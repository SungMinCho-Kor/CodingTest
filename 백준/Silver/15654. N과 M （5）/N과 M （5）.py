from itertools import permutations

n,m = map(int, input().split())
ls = list(map(int,input().split()))
ls.sort()
ls2 = list(permutations(ls,m))
for i in range(len(ls2)):
    for k in ls2[i]:
        print(k,end=" ")
    print()