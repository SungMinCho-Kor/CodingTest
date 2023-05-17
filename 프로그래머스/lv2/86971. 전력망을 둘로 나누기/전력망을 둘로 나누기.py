'''
wires를 모두 탐색하며 한개씩 빼고 for문 돌림.
for문 내용 : 하나 빼고 1로 DFS 돌림.
한번 돌린 DFS후에 visit 개수 세기
n에서 뺀 수와 visit 개수 차이가 가장 작을 때 구하면 댐.
'''

def solution(n, wires):
    answer = -1
    visit = [False * n]
    for i in range(len(wires)):
        tmp = wires[:i] + wires[i+1:]
        print(tmp)
    return answer