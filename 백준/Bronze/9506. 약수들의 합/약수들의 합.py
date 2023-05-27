
import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    ls = []
    for i in range(1,n):
        if n%i==0:
            ls.append(i)
    if sum(ls) == n:
        print(f"{n} = ",end="")
        for i in range(len(ls) - 1):
            print(f"{ls[i]} + ", end = "")
        print(f"{ls[-1]}")
    else:
        print(f"{n} is NOT perfect.")