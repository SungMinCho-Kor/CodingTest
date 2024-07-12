import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().rstrip().split()))
    target = int(sys.stdin.readline().rstrip())
    
    target_list = [0 for i in range(target + 1)]
    target_list[0] = 1
    
    for coin in coins:
        for i in range(1,target+1):
            if i-coin >= 0:
                target_list[i] += target_list[i - coin]
            
    print(target_list[target])