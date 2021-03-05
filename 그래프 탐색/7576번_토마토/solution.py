from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

board = []
tomato = []

for i in range(M):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            tomato.append((i,j))
    board.append(tmp)

def print_board(board):
    for k in board:
        print(k)
    print()

def check(board):
    max = -1
    for i in range(M):
        for j in range(N):
            if board[i][j] == 0:
                return -1
            elif max < board[i][j] :
                max = board[i][j]

    return max


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def solution(board,tomato):
    ##BFS
    result = 0
    q = deque()
    cnt = 1
    for x,y in tomato:
        q.append((x,y,cnt))

    #print_board(board)
    while q:
        #print(q)
        x,y,cnt = q.popleft()

        #print_board(board)

        for i in range(4):
            tmp_x, tmp_y = x+dx[i] , y+dy[i]
            if 0<=tmp_x<M and 0<=tmp_y<N and board[tmp_x][tmp_y]== 0:
                q.append((tmp_x,tmp_y,cnt+1))
                board[tmp_x][tmp_y] = cnt+1


    result = check(board)
    if result == -1:
        return -1
    else:
        return result -1


result = solution(board,tomato)
print(result)

