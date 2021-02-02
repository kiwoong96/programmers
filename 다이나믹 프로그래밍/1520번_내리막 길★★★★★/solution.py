import sys

M, N = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


dp = [[-1 for _ in range(N)] for _ in range(M)]

dxy = [[1,0],[0,-1],[-1,0],[0,1]]

sys.setrecursionlimit(10000)

def dfs(x,y):
    print(x,y,"dfs입장!")
    if x == M-1 and y == N-1:
        return 1
    elif dp[x][y] == -1:
        dp[x][y] = 0
        for dt in dxy:
            tmp_x, tmp_y = x+dt[0],y+dt[1]
            if 0 <= tmp_x <M and 0<= tmp_y <N:
                if arr[tmp_x][tmp_y] < arr[x][y]:

                    dp[x][y] += dfs(tmp_x,tmp_y)
    for i in range(M):
        print(dp[i])
    print()
    return dp[x][y]

print(dfs(0,0))





