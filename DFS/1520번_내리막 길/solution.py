import sys
sys.setrecursionlimit(10000)

def DFS(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0 <= nx <= M-1 and 0 <= ny <= N-1:
            if board[x][y] > board[nx][ny]:
                dp[x][y] += DFS(nx,ny)

    return dp[x][y]


M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
DFS(0,0)

print(dp[0][0])