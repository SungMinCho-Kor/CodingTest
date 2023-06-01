
'''
가장 많이겹치는 
-20 ~ -15 / -18 ~ -13 / -14 ~ -5 / -5 ~ -3
-18 ~ -15 / -14 ~ -5 / -5 ~ -3
-18 ~ -15 / -5~-5 

'''
def solution(routes):
    routes.sort()
    i = 1
    while i<len(routes):
        if routes[i-1][1]>=routes[i][0]:
            routes[i-1][0] = routes[i][0]
            if routes[i-1][1] >= routes[i][1]:
                routes[i-1][1] = routes[i][1]
            routes.pop(i)
        else:
            i+=1
    return len(routes)


print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2