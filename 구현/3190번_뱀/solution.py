import heapq
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())


board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(K):
    x,y = map(int,input().split())
    board[x][y] = 1

board[1][1] = 2
##snake

snake = deque([[1,1]])

L = int(input())
change = []

for j in range(L):
    tmp = input().strip('\n').split()
    time, dir = int(tmp[0]),str(tmp[1])
    heapq.heappush(change,(time,dir))

x = 1
y = 1
time = 0
direction = [[0,1],[-1,0],[0,-1],[1,0]]
now_direction = 0



while (0<x+direction[now_direction][0]<=N and 0<y+direction[now_direction][1]<=N):

    ##뱀의 몸위치 변경
    x,y = x+direction[now_direction][0], y+direction[now_direction][1]
    if board[x][y] == 1:
        board[x][y] = 2
        snake.append([x,y])
    elif board[x][y] == 2:
        break
    else:
        board[x][y] = 2
        snake.append([x, y])
        tmp_x,tmp_y = snake.popleft()
        board[tmp_x][tmp_y] = 0
    time += 1

    ##방향전환 확인
    #print("time : " , time,change)
    if change:
        if change[0][0] == time:
            tmp = heapq.heappop(change)
            if tmp[1] == 'D':
                if now_direction == 0: now_direction = 3
                else: now_direction -= 1

            if tmp[1] == 'L':
                if now_direction == 3: now_direction = 0
                else: now_direction += 1


    """
    for boards in board:
        print(boards)
    print()
    print(direction,now_direction)
    """

print(time+1)













