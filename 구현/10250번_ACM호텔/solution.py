import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    if N%H == 0:
        second = N//H
        first = H
    else:
        second = N//H + 1
        first = N%H
    if second < 10:
        second = '0' + str(second)
    print(str(first) + str(second))

