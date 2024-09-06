import sys
input = sys.stdin.readline
        
A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())
LCS = [[""]*len(B) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            if len(LCS[i][j-1]) > len(LCS[i-1][j]):
                LCS[i][j] = LCS[i][j-1]
            else:
                LCS[i][j] = LCS[i-1][j]
            
answer = len(LCS[-1][-1])
print(answer)
if answer > 0:
    print(LCS[-1][-1])