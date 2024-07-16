import sys

brackets = list(sys.stdin.readline().rstrip())

stack = []

answer = 0
tmp = 1
for i in range(len(brackets)):
    bracket = brackets[i]
    
    if bracket == "(":
        tmp *= 2
        stack.append(bracket)
    elif bracket == "[":
        tmp *= 3
        stack.append(bracket)
    elif bracket == ")":
        if not stack or stack[-1] != "(":
            answer = 0
            break
        if brackets[i-1] == "(":
            answer += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] != "[":
            answer = 0
            break
        if brackets[i-1] == "[":
            answer += tmp
        tmp //= 3
        stack.pop()
        
if stack:
    print(0)
else:
    print(answer)