N = int(input())
arr = []
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    arr.append(list(map(int,input().split())))



def dfs(x,y):
    if x == N-1 and y == N-1:
        #print("도착!")
        return 1
    elif dp[x][y] == -1:
        dp[x][y] = 0
        #right
        tmp_x1,tmp_y1 = x , y + arr[x][y]
        #down
        tmp_x2,tmp_y2 = x + arr[x][y] , y
        #print(tmp_x1,tmp_y1,tmp_x2,tmp_y2)
        if 0 <= tmp_x1 < N and 0 <= tmp_y1 < N : dp[x][y] += dfs(tmp_x1, tmp_y1)
        if 0 <= tmp_x2 < N and 0 <= tmp_y2 < N : dp[x][y] += dfs(tmp_x2, tmp_y2)
    #print(dp)
    return dp[x][y]


print(dfs(0,0))

