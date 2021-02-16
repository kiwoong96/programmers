from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1e9)
N,M = map(int,input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))

house = []
chicken_shop = []


for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken_shop.append((i,j))

print(house)
print(chicken_shop)


chicken_shop2 = [str(i) for i in range(len(chicken_shop))]
comb = list(map(''.join, combinations(chicken_shop2,M)))
print(comb)

result = INF
for i in comb:
    arr = [INF for _ in range(len(house))]
    for k in i:
        x, y = chicken_shop[int(k)][0], chicken_shop[int(k)][1]
        for j in range(len(house)):
            if arr[j] > abs(x-house[j][0]) + abs(y-house[j][1]):
                arr[j] = abs(x-house[j][0]) + abs(y-house[j][1])
        print(i,k,x,y,arr)
    if result > sum(arr):
        result = sum(arr)

print(result)
