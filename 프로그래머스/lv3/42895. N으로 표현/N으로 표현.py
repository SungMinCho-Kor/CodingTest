
'''
방법1 : N을 기준으로 생각
방법2 : number를 기준으로 생각

방법 1 : N이 1인경우부터 9인 경우까지 간다.
방법 2 : number가 1부터 number인 경우까지 간다.
2가 현실적

방법 2 : number가 1부터 number인 경우까지 간다.


만들 수 있는 경우 N 기준 N이 4인 경우
[1]
4
[2]
44,4+4,4*4,4/4
[3]
444, 
44+4,44-4,44*4,44/4
,4+4+4,4+4-4,(4+4)*4,(4+4)/4
, 4*4+4, 4*4-4, 4*4*4, 4*4/4, 
4/4+4,4/4-4,4/4*4,4/4/4


dp[0] = []
dp[1] = [4]
dp[2] = (44, dp[1]dp[1])
dp[3] = dp[2]dp[1]
dp[4] = dp[1]dp[3], dp[2]dp[2]
dp[5] = dp[1]dp[4], dp[2]dp[3]
'''
def solution(N, number):
    answer = 0
    numstr = ""
    dp = [()]
    i = 1
    while i<9:
        numstr += str(N)
        tmp = set()
        tmp.add(int(numstr))
        for j in range(1,i//2 + 1):
            for n in dp[j]:
                for m in dp[i-j]:
                    tmp.add(n+m)
                    if n-m>0:
                        tmp.add(n-m)
                    if m-n>0:
                        tmp.add(m-n)
                    tmp.add(n*m)
                    if n/m == int(n/m):
                        tmp.add(int(n/m))
                    if m/n == int(m/n):
                        tmp.add(int(m/n))

        dp.append(tmp)        
        if number in tmp:
            return i
        i+=1
    if i==9:
        return -1
                    
                
            
    
    
    
#     ls = [()]
#     while True:
#         ls2 = set()
#         numstr += str(N)
#         ls2.add(int(numstr))
#         for i in ls:
#             for j in i:
#                 ls2.add(j+N)
#                 if j-N>0:
#                     ls2.add(j-N)
#                 if N-j>0:
#                     ls2.add(N-j)
#                 ls2.add(j*N)
#                 if j/N == int(j/N):
#                     ls2.add(j/N)
#                 if N/j == int(N/j):
#                     ls2.add(N/j)
#         print(ls2)
#         if number in ls2:
#             return len(numstr)
#         elif len(numstr)>8:
#             return -1
#         ls.append(ls2)