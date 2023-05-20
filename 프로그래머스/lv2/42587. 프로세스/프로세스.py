def solution(priorities, location):
    queue = [(i,j) for i,j in enumerate(priorities)]
    # print(queue)
    loc = 0
    while True:
        now = queue.pop(0)
        if any(now[1]< i[1] for i in queue):
            queue.append(now)
        else:
            loc+=1
            if now[0] == location:
                return loc