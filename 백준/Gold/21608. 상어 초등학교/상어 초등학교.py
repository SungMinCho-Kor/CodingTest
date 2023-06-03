
import sys


#입력 받는 구간
n = int(sys.stdin.readline().rstrip())
sits = [[0 for _ in range(n)] for _ in range(n)]
#sits : 실제로 애들을 앉힐 좌석
students = dict()
sited = [False for _ in range(n**2 + 1)]
#sited[k] : k번 student 가 (i,j) 에 앉아 있다고 적어놓은 것. 
#           k번 student가 앉아있지 않다면 False로 초기화 되어있다. 
for i in range(n**2):
    s,s1,s2,s3,s4 = map(int,sys.stdin.readline().rstrip().split())
    students[s] = [s1,s2,s3,s4]

#좌표 이동을 위한 dx dy 선언
dx = [-1, 1, 0 , 0]
dy = [0,0,1,-1]
for student, friends in students.items():
    #favor 리스트 : student가 선호하는 친구들의 주변 값들을 하나씩 증가시킨 리스트
    #favor의 최대값을 찾으면 된다.
    favor = [[0 for _ in range(n)]for _ in range(n)]
    for friend in friends:
        if sited[friend]!=False:
            for k in range(4):
                if 0<=(sited[friend][0] + dx[k])<n and 0<=(sited[friend][1]+dy[k])<n :
                    if sits[sited[friend][0] + dx[k]][sited[friend][1]+dy[k]] == 0:
                        favor[sited[friend][0] + dx[k]][sited[friend][1]+dy[k]] += 1
    #favor는 friends 주변에 비어있는 곳에 겹치는 만큼 수치가 올라가있다.
    max_favor = max(map(max,favor))
    #max_favor : favor 내의 값들 중에서 최대값(1번 조건)
    empty_around = [[0 for _ in range(n)]for _ in range(n)]
    #empty_around : max_favor인 favor자리가 여러개일 수 있으므로
    #               max_favor인 자리의 주변에 빈 자리 개수를 넣어놓은 리스트 
    for i in range(n):
        for j in range(n):
            if favor[i][j] == max_favor and sits[i][j]==0:
                cnt=0
                for k in range(4):
                    if 0<=i+dx[k]<n and 0<=j+dy[k]<n and sits[i+dx[k]][j+dy[k]]==0:
                        cnt+=1
                empty_around[i][j] = cnt
    max_empty = max(map(max,empty_around))
    #max_empty : max_favor인 favor자리 중에서 빈자리 max 개수
    for i in range(n):
        if sited[student]!= False:
            break
        for j in range(n):
            if max_empty == empty_around[i][j] and sited[student] == False and sits[i][j]==0 and favor[i][j]==max_favor:
                sits[i][j] = student
                sited[student] = [i,j]
                break
    #max_empty이면서 빈 자리에 넣고 sited와 sits에 대입.
score = 0
for student, friends in students.items():
    cnt = 0 
    a = sited[student][0]
    b = sited[student][1]
    for i in range(4):
        if 0<=a+dx[i]<n and 0<=b+dy[i]<n and sits[a+dx[i]][b+dy[i]] in friends:
            cnt+=1
    if cnt==1:
        score+=1
    elif cnt==2:
        score+=10
    elif cnt==3:
        score+=100
    elif cnt==4:
        score+=1000
print(score)