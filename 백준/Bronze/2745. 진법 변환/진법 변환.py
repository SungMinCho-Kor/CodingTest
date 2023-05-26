
import sys

string, num = sys.stdin.readline().rstrip().split()
num = int(num)
string = list(string)
answer = 0
for i in string:
    answer*=num
    if i.isdigit():
        answer+=int(i)
    else:
        answer+=ord(i) - ord('A') + 10
print(answer)