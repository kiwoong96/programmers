from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int,input().split())
board = [[0 for _ in range(M+1)]for _ in range(N+1)]

for i in range(0,N):
    tmp = input().strip('\n')
    for j in range(0,M):
        board[i+1][j+1] = int(tmp[j])


def print_board(board):
    for i in board:
        print(i)
    print()



dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(board,x,y):
    ##BFS
    q = deque()
    q.append((x,y))
    visited = [[False for _ in range(M+1)]for _ in range(N+1)]
    visited[1][1] = True

    while q:
        now_x,now_y = q.popleft()
        if now_x == N and now_y == M:
            break
        for i in range(4):
            tmp_x, tmp_y = now_x +dx[i] , now_y + dy[i]
            if 1<=tmp_x<=N and 1<=tmp_y<=M:
                if board[tmp_x][tmp_y] != 0:
                    if visited[tmp_x][tmp_y] == False and (board[tmp_x][tmp_y] == 1 or board[tmp_x][tmp_y] > board[now_x][now_y] + 1):
                        q.append((tmp_x,tmp_y))
                        board[tmp_x][tmp_y] = board[now_x][now_y] + 1
                        visited[tmp_x][tmp_y] = True
    return board[N][M]





result = solution(board,1,1)
#print_board(board)
print(result)
