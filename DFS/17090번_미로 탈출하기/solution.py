import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


N,M = map(int,input().split())
board = [list(input().split()) for _ in range(N)]



dp = [[-1 for _ in range(M)] for _ in range(N)]

dxy = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}

def dfs(x,y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    nx, ny = x+dxy[board[x][0][y]][0],y+dxy[board[x][0][y]][1]

    dp[x][y] = dfs(nx,ny)
    return dp[x][y]
    

for i in range(N):
    for j in range(M):
        dfs(i,j)

result = 0

for i in range(N):
    result+= sum(dp[i])
print(result)