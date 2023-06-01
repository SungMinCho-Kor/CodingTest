'''
[a,b,c]
a : 섬 1
b : 섬 2
c : 섬 1 - 섬 2 cost

4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 8], [2, 3, 1]]


'''
def solution(n, costs):
    costs.sort(key= lambda x:x[2])
    ls = []
    tmp= costs.pop(0)
    ls.append(tmp[0])
    ls.append(tmp[1])
    cost = tmp[2]
    i = 0
    while len(ls)!=n:
        if costs[i][0] in ls and costs[i][1] in ls:
            i+=1 
            continue
        elif costs[i][0] in ls:
            ls.append(costs[i][1])
            cost+=costs[i][2]
            i = 0
        elif costs[i][1] in ls:
            ls.append(costs[i][0])
            cost+=costs[i][2]
            i = 0
        else:
            i+=1
    return cost