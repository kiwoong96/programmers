from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = []

for i in range(N):
    board.append(list(map(int,input().strip('\n'))))

dxy = [[0,1],[1,0],[-1,0],[0,-1]]

visited = [[False for _ in range(N)] for _ in range(N)]

##DFS

"""
def DFS(x,y):
    visited[x][y] = True

    for k in dxy:
        tmp_x, tmp_y = x+k[0], y+k[1]
        if 0<=tmp_x <N and 0<=tmp_y <N:
            if board[tmp_x][tmp_y] == 1 and visited[tmp_x][tmp_y] == False:
                board[x][y] += DFS(tmp_x,tmp_y)

    return board[x][y]

cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            result.append(DFS(i,j))


result.sort()
print(cnt)
for i in result:
    print(i)"""

##BFS

def BFS(x,y,cnt):
    cnt +=1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        tmp = queue.pop()
        for dt in dxy:
            tmp_x, tmp_y = tmp[0]+dt[0], tmp[1]+dt[1]
            if 0<=tmp_x<N and 0<=tmp_y<N and board[tmp_x][tmp_y] == 1 and visited[tmp_x][tmp_y] == False:
                cnt +=1
                queue.append((tmp_x,tmp_y))
                visited[tmp_x][tmp_y] = True

    return cnt

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == False:
            result.append(BFS(i,j,0))
            cnt += 1
print(cnt)

result.sort()

for i in result:
    print(i)