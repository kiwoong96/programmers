import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())
house = []
chicken_shop = []


for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            house.append((i,j))
        elif tmp[j] == 2:
            chicken_shop.append((i,j))

def solution(house,chicken_shop):
    chicken = list(combinations(chicken_shop,M))
    result = INF
    for c in chicken:
        distance = [INF for _ in range(len(house))]
        for cx,cy in c:
            for h in range(len(house)):
                hx, hy = house[h]
                if distance[h] > abs(cx-hx)+abs(cy-hy):
                    distance[h] =  abs(cx-hx)+abs(cy-hy)

        if result > sum(distance):
            result = sum(distance)
    return result

result = solution(house,chicken_shop)

print(result)