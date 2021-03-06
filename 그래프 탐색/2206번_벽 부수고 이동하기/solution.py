from collections import deque
import sys
input = sys.stdin.readline



N,M = map(int,input().split())
board =[]

for i in range(N):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
        if tmp[j] == 1:
            tmp[j] = -1
    board.append(tmp)


def print_board(board):
    for i in board:
        print(i)
    print()


dx = [-1,1,0,0]
dy = [0,0,1,-1]
s_x,s_y = 0,0

def solution(board,s_x,s_y):
    visited = [[[False,False] for _ in range(M)]for _ in range(M)]
    result = -1
    q = deque()
    chance = False
    cnt = 0
    q.append((cnt,chance,s_x,s_y))
    visited[s_x][s_y] = True
    print_board(board)
    while q:
        print(q)
        cnt, chance, x, y = q.popleft()
        if x == N-1 and y == M-1:
            result = cnt
        for i in range(4):
            tmp_x, tmp_y = x+dx[i], y+dy[i]
            print(tmp_x,tmp_y)
            if 0<=tmp_x<N and 0<=tmp_y<M and visited[tmp_x][tmp_y] == False:
                print("Come in",tmp_x,tmp_y)
                if board[tmp_x][tmp_y] == 0:
                    q.append((cnt+1,chance, tmp_x,tmp_y))

                elif board[tmp_x][tmp_y] == -1 and chance == False:
                    tmp_chance = True
                    q.append((cnt+1,tmp_chance,tmp_x,tmp_y))



    return result


result = solution(board,s_x,s_y)
if result == 0:
    print(-1)
else:
    print(result)