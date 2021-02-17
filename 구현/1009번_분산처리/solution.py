import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    result = 1

    for _ in range(b):
        result *= a
        result = str(result)
        result = result[-1]
        result = int(result)
    if result == 0: print(10)
    else: print(result)
