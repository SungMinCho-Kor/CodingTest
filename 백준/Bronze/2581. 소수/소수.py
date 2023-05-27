
import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

ls = [i for i in range(m,n+1)]
ls2 = []
for i in ls:
    cnt= 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt+=1
    if cnt==2:
        ls2.append(i)
if ls2:
    print(sum(ls2))
    print(min(ls2))
else:
    print(-1)