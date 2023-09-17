# '''
# 1   2   3  
# 0,0 0,1 0,2
# 4   5   6
# 1,0 1,1 1,2
# 7   8   9
# 2,0 2,1 2,2
# *   0   #
# 3,0 3,1 3,2
# '''
# def solution(numbers, hand):
#     answer = ''
#     left = [3,0]
#     right = [3,2]
#     pad = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
#     for i in numbers:
#         if i == 1 or i == 4 or i == 7:
#             left = pad[i]
#             answer += 'L'
#         elif i == 3 or i == 6 or i == 9:
#             right = pad[i]
#             answer += 'R'
#         else:
#             if abs(left[0] - pad[i][0]) + abs(left[1] - pad[i][1]) > abs(right[0] - pad[i][0]) + abs(right[1] - pad[i][1]) : 
#                 right = pad[i]
#                 answer += 'R'
#             elif abs(left[0] - pad[i][0]) + abs(left[1] - pad[i][1]) < abs(right[0] - pad[i][0]) + abs(right[1] - pad[i][1]) :
                
#                 left = pad[i]
#                 answer += 'L'
#             else:
#                 if hand == "right":
#                     right = pad[i]
#                     answer += 'R'
#                 else:
#                     left = pad[i]
#                     answer += 'L'
#     return answer








def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def solution(numbers, hand):
    answer = ""
    point = [[1,0], [0,3], [1,3], [2,3], [0,2], [1,2], [2,2], [0,1], [1,1], [2,1]]
    
    l = [0, 0]
    r = [2, 0]
    
    for num in numbers:
        tmp_l = l
        tmp_r = r
        x, y = point[num]
        
        if x == 0:
            answer += "L"
            l = point[num]
        elif x == 2:
            answer += "R"
            r = point[num]
        elif distance(point[num],r) > distance(point[num],l):
            answer += "L"
            l = point[num]
        elif distance(point[num],r) < distance(point[num],l):
            answer += "R"
            r = point[num]
        elif hand == "right":
            answer += "R"
            r = point[num]
        else:
            answer += "L"
            l = point[num]
    return answer